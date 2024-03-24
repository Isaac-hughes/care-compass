# care-compass

Care compass is a patient appointment management application.

For a full demo of the application please refer to the video submitted with the assignment.

The application has been built in accordance with the key goals set out in the assignment brief.

At a glance features include:

- Two account types, patients and admins
- Patients can create and manage accounts and appointments created by themselves
- Admins can create, manage and delete all accounts and appointments

Apart from the tables that come with django, there are two custom tables used by the application:

- Accounts
- Appointments

These tables are controlled by custom models defined the in models.py files for each app

The application was built following clean code principles with an emphasis on self documenting, readable code.

Each app has unit tests to validate behaviour; however, due to the limited time available in the project these tests are limited.

All forms within the application have validation to ensure data quality and security.

I have written all code from scratch including the .py, .js, .css and .html files.

Jquery has been used for controlling some frontend behaviour, if I had more time i would've liked to have built the frontend in react.

Modular css has been used for styling.

Templates are built with HTML.

# Set up instructions:

## Create and activate a virtual environment

python -m venv care-compass-env
care-compass-env\Scripts\activate

## Install project dependencies

pip install -r requirements.txt

## Run application

py manage.py runserver

## Run unit tests

py manage.py test

## Create admin account from terminal

py manage.py addadmin
