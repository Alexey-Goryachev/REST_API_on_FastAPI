# REST_API_on_FastAPI

This API is for saving and managing contacts.

The API uses SQLAlchemy and Alembic migrations to manage the database.

The API has the standard functionality of GRUD operations as well as additional functions:

- search for contacts by first name, last name or email.
- receive a list of contacts with birthdays for the next 7 days

To view, install the necessary packages, run the main file main.py and open localhost(http://127.0.0.7:8000/docs) in your browser.

In order to use the contacts functionality, you must first pass authorization (login -test1@example.com, password - 123456) or register a new user and log in through him.
