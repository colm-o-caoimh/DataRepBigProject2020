# DataRepBigProject2020
Data Representation: Big Project 2020

## Project Type A - Web Application
***

For this project I have chosen option A - design a web application. It links to a single database table containing data on movies. <br>

This repository contains the following files necessary to run the app:
##### server.py
Python file which implements the Rest API. The server interacts with Python Flask, mapping http requests from the browser to individual functions performing CRUD operations. It also interacts with the database via the DAO (also found in this repository).
##### movieDAO.py
Python file which connects to the database, collects the data and returns it back to the server. 
##### staticpages folder
This folder contains a html file (index.html) which builds the frontend user interface. 
##### requirements.txt
txt file containing necessary packages to allow the application to function. These can be used to set up a virtual environment.
##### dbconfig_template.py
Python file which enables flexible configuration regardless of what machine the app is being run on.
##### initdb.sql
sql file containing code for databse and table creation (my app has been deployed to pythonanywhere so this file may not be necessary)
##### pythonanywhere_link.docx
This file contains the link the hosted web app (hosted on pythonanywhere.com). There is also a little explanation as to the functionality of my app
