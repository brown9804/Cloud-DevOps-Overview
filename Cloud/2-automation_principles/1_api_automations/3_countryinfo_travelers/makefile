#Python3

##--------------------------
##    Copyright (C) 2022
##    Timna Brown  
##--------------------------

# Frames result folder
SRC = src/

#*****************************
#####    Create env/Run python script
#*****************************

env: # create env 
	python3 -m venv .venv

activate: # activate env 
	source .venv/bin/activate
	
requirements: # install libs, packages 
	pip install -r ./requirements.txt
	brew install tcl-tk
	pip install countryinfo
	pip install requests-cache retry-requests numpy pandas
	pip install openmeteo-requests
	pip install chardet2 urllib3
	pip install django-contrib-comments==1.5
	pip install opentelemetry-api
	pip install opentelemetry-sdk

setupcountryinfo: 
	./setup_config.sh

run:
	python3 $(SRC)main.py
