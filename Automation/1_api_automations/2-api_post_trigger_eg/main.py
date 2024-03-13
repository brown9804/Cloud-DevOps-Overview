#Python3


##--------------------------------Main file------------------------------------
##                         Copyright (C) 2022 
##                         Belinda Brown Ramírez 
##                         belindabrownr04@gmail.com
##--------------------------

import aiohttp
import asyncio
import time
import requests
import json 
import hashlib
import hmac
import base64
import pandas as pd 
import binascii

## Definitions 

def post_call_trigger_process(secret_key):
    secret_key = bytes(secret_key, 'UTF-8')
    url = '' 
    payload = {
       "error": "error eg",
       "name": "name eg", 
       "email": "email eg",
       "status": "status eg",
	   "type": "type eg"
    }

    response = requests.post(url, data=json.dumps(payload) )# ,headers=headers)

    print(response.status_code)
    print(response.text)

def post_call_trigger_process_headers(secret_key):
    secret_key = bytes(secret_key, 'UTF-8')
    url = ''  
    payload = {
        'name': 'Belinda',
        'last_name': 'Brown'
    }
    headers = {
        'xapi-key': '', 

        'Ocp-Apim-Subscription-Key': '', 

        'X-Hub-Signature': sig1hex,
        'Authorization': 'Basic ', 

        'Content-Type': 'application/json'
    }

    message = json.dumps(payload)
    print(message)
    print(type(message)) 

    with open('./outfile_log.txt', 'w') as outfile:
        json.dump(payload, outfile)

    message = bytes(message, 'UTF-8')
    digester = hmac.new(secret_key, message, digestmod=hashlib.sha1)
        
    sig1hex = digester.hexdigest()
    print(sig1hex) 

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.status_code)
    print(response.text)

def sha1_sign(person_name, person_id, url, secret_key):
    payload = {
        'person_id': person_id,
        'person_name': person_name
    }
    headers = {
        'xapi-key': '', #

        'Ocp-Apim-Subscription-Key': '',

        'X-Hub-Signature': sig1hex,
        'Authorization': 'Basic ', 
        
        'Content-Type': 'application/json'
    }

    message = json.dumps(payload)
    print(message)
    print(type(message)) 

    message = bytes(message, 'UTF-8')
    digester = hmac.new(secret_key, message, digestmod=hashlib.sha1)
    sig1hex = digester.hexdigest()
    print(sig1hex) 

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.status_code)
    print(response.text)

    time.sleep(5)
    
    print("After 5 seconds\n")


## -------------------------
##           MAIN    

## Post call in loop 
with open('./input_file.json') as data_file:  
    url = ''
    secret_key = ''
    person_name_df = pd.DataFrame(columns=['user_name'])
    data = json.load(data_file)
    for v in data:
        array = [v['user_name']]
        person_name_df.loc[len(person_name_df)] = array
   # print(person_name_df) # array with all the names needed 

for ind in person_name_df.index:
    person_name = person_name_df['user_name'][ind]
    person_id = person_name_df['person_id'][ind]
    # print(person_name_df['user_name'][ind])
    sha1_sign(person_name, person_id, url, secret_key)

## References 
#[1] https://bobbyhadz.com/blog/python-no-module-named-requests
#[2] https://www.geeksforgeeks.org/pandas-set_option-function-in-python/#:~:text=set_option()%20function%20in%20Python,-View%20Discussion&text=Pandas%20have%20an%20options%20system,value%20of%20a%20specified%20option.
#[3] https://stackoverflow.com/questions/49328447/display-in-python