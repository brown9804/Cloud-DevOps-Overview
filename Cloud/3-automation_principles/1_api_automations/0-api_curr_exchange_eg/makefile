# vim: set noet:

#!/usr/bin/env python3

###### API running

###### Easier make than the command line :)
###### belindabrownr04@gmail.com

######       A general utility script for Flask applications.
######  Provides commands from Flask, extensions, and the application. Loads the
######  application defined in the FLASK_APP environment variable, or from a
######  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
######  will enable debug mode.
###### $ export FLASK_APP=hello.py
###### $ export FLASK_ENV=development
###### $ flask run

all: app env 

app:
	export FLASK_APP=main.py

env:
	export FLASK_ENV=development
	flask run


####### FYI how to fixed missing separator error 
###### $vim makefile
###### after opening file with vim :%s/^[ ]\+/\t/g
###### then :wq!

