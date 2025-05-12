# Backend challenge for Una Health GmbH

## Tech/framework

* Language: ``Python 3.12.9``
* Framework: ``Django 5.2.1``
* Database: ``postgres``


## Installation

```
$ git clone https://github.com/msadour/glucose_levels_api

$ cd glucose_levels_api

$ virtualenv .venv

$ .venv/script/activate

$ pip install -r requirements.txt

$ Put .env file in glucose_level_api folder (nearby settings.py)

```

##  API Endpoints

1. Create Glucose Records from file

Endpoint: /api/v1/levels/

Method: POST

Body Parameters:

file : path_to_your_file


2. Get Glucose Records from user id

Endpoint: /api/v1/levels/user_id/<user_id>

Method: GET

Query Parameters:

* page (optional) - Page number (default: 1)

* page_size (optional) - Number of records per page (default: 10)

* limit (optional) - Number of records

* start (optional) - Records from a given date

* stop (optional) - Records until a given date


3. Get a single Glucose Record from id

Endpoint: /api/v1/levels/id/<glucose_record_id>