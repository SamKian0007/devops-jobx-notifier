# application/dataframe_plot.py
from flask import render_template, request
import plotly.express as px
import plotly.io as pio
from application.jobs_dataframe import devops_jobs_dataframe


def jobs_devops_formated():
    df = devops_jobs_dataframe("devops", 50)

    table_html = df.to_html(
        classes="table table-striped table-bordered table-hover align-middle",
        index=False,
        border=0
    )
    return render_template(
        "devops.html",
        title="open jobs for DevOps",
        header="DevOps Jobs",
        table_html=table_html,

    )
