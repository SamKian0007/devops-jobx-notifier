import pandas as pd
import os
import json
from application.jobs_dataframe import search_local_jobs, DATA_PATH

def test_search_local_jobs(tmp_path, monkeypatch):
    # create fake data file
    sample = [{"Title": "DevOps Engineer", "City": "Stockholm"}]
    data_file = tmp_path / "devops_jobs.json"
    data_file.write_text(json.dumps(sample))
    monkeypatch.setattr("application.jobs_dataframe.DATA_PATH", str(data_file))

    df = search_local_jobs("DevOps")
    assert not df.empty
    assert "Stockholm" in df.to_string()

