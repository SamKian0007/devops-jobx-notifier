def test_404_page(client):
    response = client.get("/nonexistent-page-xyz")
    assert response.status_code == 404
