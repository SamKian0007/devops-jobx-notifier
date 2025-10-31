# application/notify.py
"""Module for sending summary emails with DevOps job updates.

This module generates a summary of DevOps job data by city and emails
the results as an HTML-formatted report to predefined recipients.
"""

import pandas as pd
from application.services_providers.send_email import send_email


def send_devops_jobs_update(df: pd.DataFrame) -> tuple[str, int]:
    """Send summary email with top DevOps job data by city."""
    if df.empty:
        send_email("DevOps Jobs Update", "<p>No jobs found.</p>")
        return ("", 204)

    summary = (
        df["City"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
        .rename(columns={"index": "City", "City": "Jobs"})
        .head(10)
    )

    summary_html = summary.to_html(index=False, border=1)
    html_body = f"""
    <h2>DevOps Jobs Summary</h2>
    <p>Top 10 cities by number of job ads:</p>
    {summary_html}
    <br>
    <p>Total jobs analyzed: <b>{len(df)}</b></p>
    """
    send_email("DevOps jobs update from Job Explorer", html_body)
    return ("", 204)
