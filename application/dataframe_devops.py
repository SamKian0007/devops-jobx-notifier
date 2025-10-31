# application/dataframe_devops.py
"""Module for generating and rendering formatted DevOps jobs table.

This module retrieves DevOps job listings as a pandas DataFrame and
renders them into an interactive HTML table using a Flask template.
"""

from flask import render_template, request
from application.jobs_dataframe import devops_jobs_dataframe


def jobs_devops_formated(keyword="devops"):
    """Fetch DevOps jobs and render as HTML table."""
    df = devops_jobs_dataframe(keyword, 50)
    table_html = df.to_html(
        classes="table table-striped table-bordered table-hover align-middle",
        index=False,
        border=0
    )
    return render_template(
        "devops.html",
        title=f"Open jobs for {keyword.title()}",
        header=f"{keyword.title()} Jobs",
        table_html=table_html,
    )
