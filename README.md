# REST_API_on_FastAPI

This API is for saving and managing contacts.

The API uses SQLAlchemy and Alembic migrations to manage the database.

The API has the standard functionality of GRUD operations as well as additional functions:

- search for contacts by first name, last name or email.
- receive a list of contacts with birthdays for the next 7 days

To view, run the main file main.py and open localhost(http://127.0.0.7:8000/docs) in the browser
