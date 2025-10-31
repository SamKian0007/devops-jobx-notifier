# local_search.py
"""Module for performing and displaying local DevOps job searches.

This module enables keyword-based searches on locally saved DevOps job data
and renders the results as an HTML table within a Flask template.
"""

import os
import pandas as pd
from flask import render_template, request

DATA_PATH = os.path.join("data", "devops_jobs.json")


def search_local_jobs(keyword: str = "") -> pd.DataFrame:
    """Return locally saved jobs filtered by keyword."""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()
    df = pd.read_json(DATA_PATH)
    if not keyword:
        return df
    keyword_lower = keyword.lower()
    mask = df.apply(lambda col: col.astype(
        str).str.lower().str.contains(keyword_lower, na=False))
    return df[mask.any(axis=1)]


def render_local_search_page():
    """Render filtered job results as HTML."""
    keyword = request.args.get("keyword", "").strip()
    df = search_local_jobs(keyword)
    table_html = df.to_html(
        classes="table table-striped table-bordered table-hover align-middle",
        index=False,
        border=0
    )
    return render_template(
        "devops.html",
        title=f"Local Search Results for '{keyword or 'All'}'",
        header=f"Local Search: {keyword or 'All Jobs'}",
        table_html=table_html,
    )
