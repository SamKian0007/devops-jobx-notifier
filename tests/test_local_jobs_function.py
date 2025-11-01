import pandas as pd
import os
import json
from application.jobs_dataframe import search_local_jobs, DATA_PATH

"""
This module tests the local job search function that reads data from
a JSON file. It ensures that the `search_local_jobs` function correctly
loads and filters job listings from a mock dataset stored in a temporary file.
"""


def test_search_local_jobs(tmp_path, monkeypatch):
    """Test that search_local_jobs reads and returns matching job entries."""
    sample = [{"Title": "DevOps Engineer", "City": "Stockholm"}]
    data_file = tmp_path / "devops_jobs.json"
    data_file.write_text(json.dumps(sample))
    monkeypatch.setattr("application.jobs_dataframe.DATA_PATH", str(data_file))

    df = search_local_jobs("DevOps")
    assert not df.empty
    assert "Stockholm" in df.to_string()
