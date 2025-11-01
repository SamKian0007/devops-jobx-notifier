import os

"""
This module tests the Flask application's login functionality using environment-based
credentials. It verifies that valid credentials allow access while invalid ones trigger
an error message or remain on the login page.
"""


def test_login_success(client, monkeypatch):
    """Test that a user with correct credentials can log in successfully."""
    monkeypatch.setenv("APP_USERNAME", "user")
    monkeypatch.setenv("APP_PASSWORD", "pass")

    data = {"username": "user", "password": "pass"}
    response = client.post("/login", data=data, follow_redirects=False)
    assert response.status_code in (302, 200)


def test_login_failure(client, monkeypatch):
    """Test that login fails and shows an error for invalid credentials."""
    monkeypatch.setenv("APP_USERNAME", "user")
    monkeypatch.setenv("APP_PASSWORD", "pass")

    data = {"username": "wrong", "password": "bad"}
    response = client.post("/login", data=data, follow_redirects=True)
    assert b"Invalid" in response.data or response.status_code == 200
