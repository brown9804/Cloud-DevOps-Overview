#Python3


##--------------------------------Main file------------------------------------
##                         Copyright (C) 2022 
##                         Belinda Brown Ramírez 
##                         belindabrownr04@gmail.com
##-----------------------------------------------------------------------------


# Importing packages 
import os
import glob
import logging
import sys
import openpyxl
from tqdm import tqdm
from datetime import date
import time
import prettytable
from fastapi import Depends, FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk  
import pandas as pd
import numpy as np

## Definitions
def preprocessing_data(filename, column_name, column_id):            
    source_df = pd.read_csv(filename, sep=',', encoding='utf-8', engine='python',error_bad_lines=False) 

    source_df[column_name] = [str(i).replace(" ", "") for i in source_df[column_name]]
    source_df = source_df.astype({column_name:'float64'})
    source_df = source_df.drop_duplicates(subset=column_id)   
    curr_df = source_df.copy()
    return curr_df

def apply_by_row(exchange_df, curr_column_0, new_curr, amount_column, std_amount_column):
    exchange_df[std_amount_column] = exchange_df.apply(lambda row : converter.convert(row[curr_column_0], new_curr, row[amount_column]), axis = 1)
    return exchange_df

def df_export_to_csv(source_df, output_file_name_with_path):
    source_df.to_csv(output_file_name_with_path, index=False)    

app = FastAPI()

url = 'https://api.exchangerate-api.com/v4/latest/USD'
router = InferringRouter()  # Step 1: Create a route

@cbv(router)  # Step 2: Create and decorate a class to hold the endpoints
class RealTimeCurrencyConverter():
    # Step 3: Add dependencies as class attributes
    @router.get("/curr_exchange_csv_api")       
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 

        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount 

app.include_router(router)   

converter = RealTimeCurrencyConverter(url)

exchange_df = preprocessing_data('./objects_data_small_slide.csv', 'Amount', 'Object ID')

new_curr_df = apply_by_row(exchange_df, 'Currency', 'USD', 'Amount', 'std_amount_column')

df_export_to_csv(new_curr_df, './new_curr_exchanged_data.csv')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
