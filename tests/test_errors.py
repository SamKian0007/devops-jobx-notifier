"""
This test verifies that the application correctly handles requests
to non-existent routes by returning an HTTP 404 status code. It ensures
the app's error handling is properly configured for unknown endpoints.
"""


def test_404_page(client):
    response = client.get("/nonexistent-page-xyz")
    assert response.status_code == 404
