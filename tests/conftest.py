import pytest
from application.app import app

"""
This module contains pytest setup for the application testing environment.
It defines a reusable test client fixture that allows simulated HTTP requests
to the Flask application without running a live server. The fixture ensures
the app runs in testing mode, providing isolated and repeatable test cases.
"""


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
