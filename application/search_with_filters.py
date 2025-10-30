from flask import Blueprint, render_template, request
from application.jobs_dataframe import devops_jobs_dataframe

bp = Blueprint("filters", __name__, url_prefix="/jobs")

@bp.get("/filter")
def jobs_filter():
    keyword = request.args.get("keyword", "devops")
    location = request.args.get("location", "")
    remote = request.args.get("remote", "")
    limit = int(request.args.get("limit", 20))
    offset = int(request.args.get("offset", 0))

    # Fetch jobs dataframe
    df = devops_jobs_dataframe(keyword, limit)

    # Optional basic filtering (if those columns exist)
    if location:
        df = df[df["City"].str.contains(location, case=False, na=False)]
    if remote.lower() == "true":
        df = df[df["Employment"].str.contains("remote", case=False, na=False)]
    elif remote.lower() == "false":
        df = df[~df["Employment"].str.contains("remote", case=False, na=False)]

    # Apply offset manually
    df = df.iloc[offset:]

    table_html = None
    if not df.empty:
        table_html = df.to_html(
            classes="table table-striped table-bordered table-hover align-middle text-center",
            index=False,
            border=0
        )

    return render_template(
        "jobs_filter.html",
        title="Filter Jobs",
        header="Filter Jobs",
        table_html=table_html
    )
