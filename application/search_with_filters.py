# search_with_filters.py
"""Module defining blueprint for filtered job search functionality.

This module provides a Flask blueprint that handles job filtering
based on user-specified parameters such as keyword, location, remote
option, and result limit. Filtered job results are rendered as an
HTML table in the template.
"""

from flask import Blueprint, render_template, request
from application.jobs_dataframe import devops_jobs_dataframe

bp = Blueprint("filters", __name__, url_prefix="/jobs")


@bp.get("/filter")
def jobs_filter():
    """Fetch, filter, and render job results based on query parameters."""
    keyword = request.args.get("keyword", "devops").strip()
    location = request.args.get("location", "").strip()
    remote = request.args.get("remote", "")
    limit_arg = request.args.get("limit", "20")

    try:
        limit = max(1, min(int(limit_arg), 100))
    except ValueError:
        limit = 20

    try:
        df = devops_jobs_dataframe(keyword, limit + 1)
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        df = None

    if df is not None and not df.empty:
        if location:
            df = df[df["City"].str.contains(location, case=False, na=False)]
        if remote.lower() == "true":
            df = df[df["Employment"].str.contains(
                "remote", case=False, na=False)]
        elif remote.lower() == "false":
            df = df[~df["Employment"].str.contains(
                "remote", case=False, na=False)]

        table_html = df.to_html(
            classes="table table-striped table-bordered table-hover align-middle text-center",
            index=False,
            border=0
        )
    else:
        table_html = "<p class='text-muted'>No results found or invalid input.</p>"

    return render_template(
        "jobs_filter.html",
        title="Filter Jobs",
        header=" ",
        table_html=table_html
    )
