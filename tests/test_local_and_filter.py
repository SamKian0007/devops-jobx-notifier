import pandas as pd


def test_local_search_page(client, monkeypatch):
    # mock local file reading
    mock_df = pd.DataFrame([{"Title": "DevOps Eng", "City": "Stockholm"}])
    monkeypatch.setattr(
        "application.local_search.search_local_jobs", lambda k="": mock_df)

    response = client.get("/jobs/devops/local-search?keyword=DevOps")
    assert response.status_code == 200
    assert b"Stockholm" in response.data


def test_jobs_filter(client, monkeypatch):
    # mock job fetch with two cities
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
