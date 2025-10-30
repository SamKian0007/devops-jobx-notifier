import os
import pandas as pd
from flask import render_template, request

# Reuse the same saved JSON path as in jobs_dataframe.py
DATA_PATH = os.path.join("data", "devops_jobs.json")


def search_local_jobs(keyword: str = "") -> pd.DataFrame:
    """Search locally saved jobs by keyword across all columns."""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()  # No saved file yet

    df = pd.read_json(DATA_PATH)
    if not keyword:
        return df

    keyword_lower = keyword.lower()
    mask = df.apply(lambda col: col.astype(
        str).str.lower().str.contains(keyword_lower, na=False))
    filtered_df = df[mask.any(axis=1)]
    return filtered_df


def render_local_search_page():
    """Flask view logic: get keyword, filter DataFrame, render HTML."""
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
