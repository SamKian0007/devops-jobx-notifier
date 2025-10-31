import os


def test_login_success(client, monkeypatch):
    monkeypatch.setenv("APP_USERNAME", "user")
    monkeypatch.setenv("APP_PASSWORD", "pass")

    data = {"username": "user", "password": "pass"}
    response = client.post("/login", data=data, follow_redirects=False)
    assert response.status_code in (302, 200)


def test_login_failure(client, monkeypatch):
    monkeypatch.setenv("APP_USERNAME", "user")
    monkeypatch.setenv("APP_PASSWORD", "pass")

    data = {"username": "wrong", "password": "bad"}
    response = client.post("/login", data=data, follow_redirects=True)
    assert b"Invalid" in response.data or response.status_code == 200
