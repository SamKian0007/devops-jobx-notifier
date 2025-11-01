import pandas as pd

"""
This module tests local job search and job filtering routes in the Flask app.
It uses mocked data and monkeypatching to isolate functionality and verify
correct handling of search queries and filtered job listings.
"""


def test_local_search_page(client, monkeypatch):
    """Test that the local search route returns correct local job data."""
    mock_df = pd.DataFrame([{"Title": "DevOps Eng", "City": "Stockholm"}])
    monkeypatch.setattr(
        "application.local_search.search_local_jobs", lambda k="": mock_df)

    response = client.get("/jobs/devops/local-search?keyword=DevOps")
    assert response.status_code == 200
    assert b"Stockholm" in response.data


def test_jobs_filter(client, monkeypatch):
    """Test that the job filter route correctly filters and returns job results."""
    def mock_fetch_jobs(keyword, limit):
        return [
            {"headline": "DevOps", "employer": {"name": "A"},
             "workplace_address": {"municipality": "Stockholm"},
             "publication_date": "2025-10-31",
             "employment_type": {"label": "Remote"},
             "duration": {"label": "Permanent"},
             "experience_required": True,
             "webpage_url": "https://example.com/job"}
        ]
    monkeypatch.setattr(
        "application.jobs_dataframe.fetch_jobs", mock_fetch_jobs)

    response = client.get(
        "/jobs/filter?keyword=devops&location=Stockholm&remote=true")
    assert response.status_code == 200
    assert b"Stockholm" in response.data
