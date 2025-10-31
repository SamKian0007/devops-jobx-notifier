def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Job" in response.data or b"Home" in response.data


def test_login_redirect(client):
    response = client.get("/login", follow_redirects=False)
    assert response.status_code in (302, 200)
