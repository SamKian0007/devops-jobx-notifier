# application/notify.py

from __future__ import annotations
import pandas as pd
from application.services_providers.send_email import send_email

def send_devops_jobs_update(df: pd.DataFrame) -> tuple[str, int]:
    """
    Pure function that sends the DevOps jobs summary email based on a DataFrame.
    Returns the same Flask-style response tuple used by the route.
    """
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
