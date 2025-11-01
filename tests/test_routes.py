"""
This module tests the application's basic routes to ensure core pages
like the home and login endpoints respond correctly and are accessible.
"""


def test_home_page(client):
    """Test that the home page loads successfully and displays expected content."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Job" in response.data or b"Home" in response.data


def test_login_redirect(client):
    """Test that the login route is reachable or redirects properly."""
    response = client.get("/login", follow_redirects=False)
    assert response.status_code in (302, 200)
