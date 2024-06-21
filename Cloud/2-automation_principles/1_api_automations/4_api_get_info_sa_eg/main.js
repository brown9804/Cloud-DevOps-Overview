// Example on how to create a call to an storage account to get data from storage table 
const storage_account_name = "storage-account-name";

// Def - Get information from storage table
const get_data_from_sa_table = async (inf_id, inf_name, parameter_select, table_name) => {
    try {
        const connection_string = "value here"; // set config variable name in case this is used with an web app -> process.env[""];
        const tableService = storage_account_name.createTableService(connection_string);
        let query_to_table = new storage_account_name.TableQuery()
            .where("inf_name eq ?", inf_name) // between "" must fit how looks within the storage table 
            .and("parameter_select eq ?", parameter_select)
            .and("inf_id eq ?", inf_id);

        return new Promise((resolve, reject) => {
            tableService.queryEntities(
                table_name,
                query_to_table,
                null,
                (error, result, response) => {
                    if (!error) {
                        resolve(response.body.value);
                    } else {
                        reject(error);
                    }
                }
            );
        });
    } catch (err) {
        console.error(err);
        throw err;
    }
};

module.exports = async function (context, req) {
    context.log("Get Data from Storage Account based on selected params");

    try {
        let output_right_schema;
        let parameter_select = filter_YN.toLowerCase().includes("no") ? "No" : "Yes" && filter_YN;
        const inf_id = (req.body && req.body.inf_id) || req.query_to_table.inf_id; // get id
        const inf_name =
            (req.body && req.body.inf_name) || req.query_to_table.inf_name; // get name
        const filter_YN =
            (req.body && req.body.filter_YN) || req.query_to_table.filter_YN; // get if filter is required or not

        // Checking common variables
        if (inf_id && inf_name) {
            let output_from_storage = [];
            let response = await get_data_from_sa_table(inf_id, inf_name, parameter_select);

            context.log("******************");
            context.log(response);

            output_from_storage = response.map((row) => ({
                name: row["RowKey"], // mandatory from storage table
                label: row["PartitionKey"], // mandatory from storage table
            }));
        } else {
            context.res = { status: 400, body: "Error: Information ID and Name are expected ... " };
        }

        context.res = { body: output_right_schema || [] };
    } catch (err) {
        context.log(err);
        context.res = { status: 500, body: err };
    }
};
