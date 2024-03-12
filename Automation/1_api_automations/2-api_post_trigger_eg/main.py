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
from Crypto.Hash import HMAC, MD5

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
