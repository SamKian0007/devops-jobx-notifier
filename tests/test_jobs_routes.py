import pandas as pd


def test_jobs_devops(client, monkeypatch):
    # mock the API data fetch
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
