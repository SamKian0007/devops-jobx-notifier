import pandas as pd


def test_notify_users(client, monkeypatch):
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

    called = {}

    def mock_send_email(subject, body):
        called["subject"] = subject
        called["body"] = body

    monkeypatch.setattr(
        "application.jobs_dataframe.fetch_jobs", mock_fetch_jobs)
    monkeypatch.setattr("application.notify.send_email", mock_send_email)

    response = client.post("/jobs/devops/notify")
    assert response.status_code == 204
    assert "DevOps" in called["subject"]
