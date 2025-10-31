# application/jobs_dataframe.py
"""Module for fetching and managing DevOps job data.

This module retrieves DevOps job listings from an external API, stores them
locally as JSON, and provides utility functions to load and search the data
as pandas DataFrames.
"""

import os
import pandas as pd
from application.services_providers.jsearch import fetch_jobs

DATA_PATH = os.path.join("data", "devops_jobs.json")


def devops_jobs_dataframe(keyword: str = "devops", limit: int = 50) -> pd.DataFrame:
    """Fetch job data via API, save to JSON, and return as DataFrame."""
    hits = fetch_jobs(keyword, limit)
    rows = [{
        "Title": h.get("headline"),
        "Employer": h.get("employer", {}).get("name"),
        "City": h.get("workplace_address", {}).get("municipality"),
        "Published": h.get("publication_date"),
        "Employment": h.get("employment_type", {}).get("label"),
        "Duration": h.get("duration", {}).get("label"),
        "Experience Required": h.get("experience_required"),
        "Apply URL": h.get("webpage_url"),
    } for h in hits]
    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    df.to_json(DATA_PATH, orient="records", indent=2)
    return df


def search_local_jobs(keyword: str = "") -> pd.DataFrame:
    """Search locally saved jobs (in /data/devops_jobs.json) by keyword."""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()
    df = pd.read_json(DATA_PATH)
    if not keyword:
        return df
    keyword_lower = keyword.lower()
    mask = df.apply(lambda col: col.astype(
        str).str.lower().str.contains(keyword_lower, na=False))
    return df[mask.any(axis=1)]
