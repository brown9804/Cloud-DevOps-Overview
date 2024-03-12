import pandas as pd 
from multiprocessing.resource_sharer import stop
import numpy as np
from datetime import date
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from IPython.display import display
import requests
# python3 -m pip install requests

## Definitions 
def reading_csv_data(filename):
    source_df = pd.read_csv(filename, sep=',', encoding='utf-8', engine='python',error_bad_lines=False) 
    return source_df

def mapping_data(dataframe):
    head = pd.DataFrame(dataframe.iloc[:3])
    display(head)
    
    output = {}
    output['Column Names'] = dataframe.columns.values.tolist()
    pd.set_option('display.max_colwidth', None)
    column_names = pd.DataFrame(data=output)
    display(column_names)
    
    output = {}
    output['Data Types'] = dataframe.dtypes
    pd.set_option('display.max_colwidth', None)
    column_dtypes = pd.DataFrame(data=output)
    display(column_dtypes)
    
    output = {}
    output['Null Values'] = dataframe.isna().sum()  # #  Is null # this is to validate the amount of rows within a columns that carry information
    pd.set_option('display.max_colwidth', None)
    null_values = pd.DataFrame(data=output)
    display(null_values)

def get_request(url, auth):
    # headers
    headers = {
        'xapi-key': '', # optional
        'Ocp-Apim-Subscription-Key': '', # optional
        'Authorization': 'Bearer  '+auth # mandatory 
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)

    time.sleep(10)

    print("After 10 seconds\n")

    logs = pd.DataFrame()
    logs = logs[[response.text]]


## -------------------------
##           MAIN
## Get request 
auth = ''
url = 'https://github.com/brown9804/SDLC-Cloud_Lpath/blob/main/Automation/1_api_automations/0-api_curr_exchange_eg/main.py'
get_request(url, auth)



