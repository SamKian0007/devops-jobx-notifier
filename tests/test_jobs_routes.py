import pandas as pd

"""
This module tests the Flask application's job-related routes using mocked data.
It ensures the `/jobs/devops` and `/jobs/devops/plot` endpoints return correct
responses and expected job details without relying on live API calls.
"""


def test_jobs_devops(client, monkeypatch):
    """Test that the /jobs/devops route renders job listings correctly."""
    def mock_fetch_jobs(keyword, limit):
        return [
            {"headline": "DevOps Engineer", "employer": {"name": "TechCorp"},
             "workplace_address": {"municipality": "Stockholm"},
             "publication_date": "2025-10-31",
             "employment_type": {"label": "Full time"},
             "duration": {"label": "Permanent"},
             "experience_required": True,
             "webpage_url": "https://example.com/job1"}
        ]

    monkeypatch.setattr(
        "application.jobs_dataframe.fetch_jobs", mock_fetch_jobs)

    response = client.get("/jobs/devops")
    assert response.status_code == 200
    assert b"DevOps Engineer" in response.data


def test_jobs_devops_plot(client, monkeypatch):
    """Test that the /jobs/devops/plot route returns correct location data."""
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

    response = client.get("/jobs/devops/plot")
    assert response.status_code == 200
    assert b"Stockholm" in response.data
