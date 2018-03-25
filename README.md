# web-common

A common website backend for all my lab website projects

#### Folder Structure

/labsite: contains the main django project  
/common: application for the lab website
/static: resources for website

#### Requirements

* django 2.0.3
* django-grappelli 2.11.1

#### Overview

The code in this repository uses the [django](https://www.djangoproject.com/) framework. Please read the django documentation for a better overview.

The main files of interest are:  
* admin.py: contains the definitions for each model in the admin panel
* models.py: definitions for each data model
* urls.py: urls for each viewport
* views.py: defines views for each webpage
