# application/dataframe_plot.py
from flask import render_template, request
import plotly.express as px
import plotly.io as pio
from application.jobs_dataframe import devops_jobs_dataframe


def jobs_devops_plot():
    df = devops_jobs_dataframe("devops", 50)

    chart_html = ""
    if not df.empty:
        city_counts = (
            df.assign(City=df["City"].fillna("Unknown"))
              .groupby("City")
              .size()
              .reset_index(name="Jobs")
              .sort_values("Jobs", ascending=False)
              .head(12)
        )
        fig = px.bar(city_counts, x="City", y="Jobs",
                     title="DevOps job ads by city (top 12)")
        fig.update_layout(height=450, margin=dict(l=20, r=20, t=60, b=20))
        chart_html = pio.to_html(fig, full_html=False, include_plotlyjs="cdn")

    table_html = df.to_html(
        index=False, border=1) if not df.empty else "<p>No jobs found.</p>"
    message = "Emails sent to the recipients list." if request.args.get(
        "sent") == "1" else None

    return render_template(
        "devops.html",
        title="DevOps Jobs — Plot",
        header="DevOps Jobs (JobTech API)",
        table_html=table_html,
        chart_html=chart_html,
        message=message,
    )
