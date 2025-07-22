# Country Information for Travelers (API integration)

Costa Rica

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-07-11

----------

> This is designed to provide users with a comprehensive overview of the country, including general information, COVID-19 data, weather details based on latitude and longitude, and an overview of the country's currency exchange rates.

## Wiki
- [Country Info](https://pypi.org/project/countryinfo/), and [repo](https://github.com/porimol/countryinfo.git)
- [Countries flags API](https://www.countryflags.io)
- [Covid information](https://www.worldometers.info/coronavirus/country/)
- [Currency conversion](https://pypi.org/project/CurrencyConverter/)
- [Weather API](https://open-meteo.com/)
  - *https://openweathermap.org/api*
  - *https://www.worldometers.info/*
- [Open Telemetry for Python](https://opentelemetry.io/docs/languages/python/)
- [opentelemetry.trace package](https://opentelemetry-python.readthedocs.io/en/latest/api/trace.html)
- [Manual instrumentation for OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/instrumentation/)
- [Guide on Develop Azure Functions by using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=node-v4%2Cpython-v2%2Cisolated-process&pivots=programming-language-csharp#x86-emulation-on-arm64)


## Setup

Please follow the makefile instructions at this location. And make sure countryinfo module is cloned before started.

~~~
make env
make activate
make setupcountryinfo
make run
~~~

Example, using Spain data:

| <!-- -->    |
|-------------|
| <img width="700" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/3cbdc543-56dc-46e1-a63b-668b5c87e3b0" alt="country inf"/> |  
| <img width="700" src="https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/ffa0287b-e5a2-4ad2-a397-7868bc3a7d10" alt="Currency  and Weather"/> | 

## With OpenTelemetry Instrumentation

~~~
Which country would you like information about?
Spain

************ Country - General Information ***********************

                    Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Values
                   Country Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Spain
Other spelling for country name                                                                                                                                                                                                                                                                                                                                                                                                                                                           [ES, Kingdom of Spain, Reino de España]
                        Capital                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Madrid
                      Provinces [A Coruña, Álava, Albacete, Alicante, Almería, Asturias, Ávila, Badajoz, Balearic Islands, Barcelona, Biscay, Burgos, Cáceres, Cádiz, Cantabria, Castellón, Ciudad Real, Córdoba, Cuenca, Gipuzkoa, Girona, Granada, Guadalajara, Huelva, Huesca, Jaén, La Rioja, Las Palmas, León, Lleida, Lugo, Madrid, Málaga, Murcia, Navarre, Ourense, Palencia, Pontevedra, Salamanca, Santa Cruz de Tenerife, Segovia, Seville, Soria, Tarragona, Teruel, Toledo,  Valencia, Valladolid, Zamora, Zaragoza]
                         Region                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Europe
                      Subregion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Southern europe
                       Currency                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             [EUR]
                      Languages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              [es]
                        Borders                                                                                                                                                                                                                                                                                                                                                                                                                                                                         [AND, FRA, GIB, PRT, MAR]
                   Calling Code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              [34]
                           Area                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            505992
                     Population                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          46507760
                       Lat/Long                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [40.416705, -3.703582]
                           Code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ES

************ Country - Covid Data ***********************

{'Total Cases': '13,914,811       ', 'Recovered Cases': '13,762,417', 'Total Deaths': '121,760'}

************ Country - Weather Information ***********************

Coordinates 40.41999816894531°N -3.6999998092651367°E
Elevation 666.0 m asl
Timezone None None
Timezone difference to GMT+0 0 s
                       date  temperature_2m
0 2024-03-19 00:00:00+00:00       17.115000
1 2024-03-19 01:00:00+00:00       16.565001
2 2024-03-19 02:00:00+00:00       15.764999
3 2024-03-19 03:00:00+00:00       16.014999
4 2024-03-19 04:00:00+00:00       15.264999

************ Country - Currency Convert ***********************

Into which currency would you like to convert?
{
    "name": "span_country_info",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x29f451e7453417d0",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0x83505264fb5e3fc1",
    "start_time": "2024-03-19T21:00:00.984521Z",
    "end_time": "2024-03-19T21:00:01.038606Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation0": "Ok - Get information from CountryInfo",
        "operation1": "Ok - Append country information to list",
        "operation2": "Ok - Store information into dataframe"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "Country_General_Inf",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x83505264fb5e3fc1",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xa9fe995e56a5ea60",
    "start_time": "2024-03-19T21:00:00.984195Z",
    "end_time": "2024-03-19T21:00:01.041551Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "span_covid_data",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x7302896895fcd04c",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0x4144afc784ce1630",
    "start_time": "2024-03-19T21:00:01.041681Z",
    "end_time": "2024-03-19T21:00:02.088010Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation0": "Ok - Cast country name to lowerCase",
        "operation1": "Ok - No need to replace empty space for - ",
        "operation2": "Ok - get worldometers country's covid data",
        "operation3": "Ok - converting the text",
        "operation4": "Ok - finding meta info for cases",
        "operation5": "Ok - getting total cases number",
        "operation6": "Ok - getting recovered cases number",
        "operation7": "Ok - getting deaths cases number",
        "operation8": "Ok - whole data in place"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "Country_CovidData",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x4144afc784ce1630",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xa9fe995e56a5ea60",
    "start_time": "2024-03-19T21:00:01.041627Z",
    "end_time": "2024-03-19T21:00:02.088952Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "span_capital_weather",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x422fae027683a48e",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xccd32033def63dab",
    "start_time": "2024-03-19T21:00:02.089397Z",
    "end_time": "2024-03-19T21:00:02.958786Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation0": "Ok - Setup the Open-Meteo API client with cache and retry on error",
        "operation1": "Ok - Call Open-Meteo API",
        "operation2": "Ok - Process first location. Add a for-loop for multiple locations or weather models",
        "operation3": "Ok - Process hourly data",
        "operation4": "Ok - Store data into Dataframe"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "Country_WeatherInformation",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0xccd32033def63dab",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xa9fe995e56a5ea60",
    "start_time": "2024-03-19T21:00:02.089031Z",
    "end_time": "2024-03-19T21:00:02.961826Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
USD
How much money would you like to convert?
100
Considering which YEAR for the exchange?
2024
Considering which MONTH for the exchange?
2
Considering which DAY for the exchange?
12
107.72999999999999 EUR to USD is: 107.72999999999999
At 2024/2/12
{
    "resource_metrics": [
        {
            "resource": {
                "attributes": {
                    "telemetry.sdk.language": "python",
                    "telemetry.sdk.name": "opentelemetry",
                    "telemetry.sdk.version": "1.23.0",
                    "service.name": "unknown_service"
                },
                "schema_url": ""
            },
            "scope_metrics": [
                {
                    "scope": {
                        "name": "country_info_app_global_meterprovider",
                        "version": "",
                        "schema_url": ""
                    },
                    "metrics": [
                        {
                            "name": "work.counter",
                            "description": "Counts the amount of work done",
                            "unit": "1",
                            "data": {
                                "data_points": [
                                    {
                                        "attributes": {
                                            "work.type": "country_info"
                                        },
                                        "start_time_unix_nano": 1710882000984390000,
                                        "time_unix_nano": 1710882010506357000,
                                        "value": 1
                                    },
                                    {
                                        "attributes": {
                                            "work.type": "covid_data"
                                        },
                                        "start_time_unix_nano": 1710882000984390000,
                                        "time_unix_nano": 1710882010506357000,
                                        "value": 1
                                    },
                                    {
                                        "attributes": {
                                            "work.type": "capital_weather"
                                        },
                                        "start_time_unix_nano": 1710882000984390000,
                                        "time_unix_nano": 1710882010506357000,
                                        "value": 1
                                    },
                                    {
                                        "attributes": {
                                            "work.type": "convert_currency"
                                        },
                                        "start_time_unix_nano": 1710882000984390000,
                                        "time_unix_nano": 1710882010506357000,
                                        "value": 1
                                    }
                                ],
                                "aggregation_temporality": 2,
                                "is_monotonic": true
                            }
                        }
                    ],
                    "schema_url": ""
                }
            ],
            "schema_url": ""
        }
    ]
}
{
    "name": "span_convert_currency",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0x0101e8a0eff5e1be",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xdd82d47940f359ab",
    "start_time": "2024-03-19T21:00:10.362301Z",
    "end_time": "2024-03-19T21:00:10.504280Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation0": "Ok - Call CurrencyConverter",
        "operation1": "Ok - Currency Exchanged"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "Country_CurrencyConvert",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0xdd82d47940f359ab",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xa9fe995e56a5ea60",
    "start_time": "2024-03-19T21:00:02.961950Z",
    "end_time": "2024-03-19T21:00:10.506232Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [
        {
            "name": "Input1 - Asking for ToCurrency exchange ...",
            "timestamp": "2024-03-19T21:00:02.962060Z",
            "attributes": {}
        },
        {
            "name": "Input2 - Asking for Amount of Money for exchange ...",
            "timestamp": "2024-03-19T21:00:05.465606Z",
            "attributes": {}
        },
        {
            "name": "Input3 - Asking for YEAR of exchange ...",
            "timestamp": "2024-03-19T21:00:06.620951Z",
            "attributes": {}
        },
        {
            "name": "Input4 - Asking for MONTH of exchange ...",
            "timestamp": "2024-03-19T21:00:08.236853Z",
            "attributes": {}
        },
        {
            "name": "Input5 - Asking for DAY of exchange ...",
            "timestamp": "2024-03-19T21:00:09.467426Z",
            "attributes": {}
        }
    ],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
{
    "name": "Country_Information_For_Travellers",
    "context": {
        "trace_id": "0x6908e6615ea20ccb8349158a18b7a428",
        "span_id": "0xa9fe995e56a5ea60",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-03-19T20:59:59.611590Z",
    "end_time": "2024-03-19T21:00:10.506248Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [
        {
            "name": "Input0 - Asking for Country Name ...",
            "timestamp": "2024-03-19T20:59:59.611606Z",
            "attributes": {}
        }
    ],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.23.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
~~~

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1276-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-22</p>
</div>
<!-- END BADGE -->
