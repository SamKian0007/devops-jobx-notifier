# app.py
from flask import Flask, render_template, session, url_for, redirect, request
from dotenv import load_dotenv

from application.jobs_dataframe import devops_jobs_dataframe
from application.dataframe_plot import jobs_devops_plot
from application.dataframe_devops import jobs_devops_formated
from application.search_with_filters import bp as filters_bp
from application.local_search import render_local_search_page
from application.notify import send_devops_jobs_update
from application.login import bp as auth_bp
import os

load_dotenv()

app = Flask(__name__)
# needed for session/flash
app.secret_key = os.getenv("SECRET_KEY", "change-me")
app.register_blueprint(auth_bp)
app.register_blueprint(filters_bp)


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/login")
def login():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("login.html", title="login", header="Job Explorer !")


@app.get("/jobs/filter")
def jobs_filter():
    return render_template("jobs_filter.html", title="Filter Jobs", header="Filter Jobs")


@app.get("/jobs/devops")
def jobs_devops():
    keyword = request.args.get("keyword", "devops")
    return jobs_devops_formated(keyword)


@app.get("/jobs/devops/local-search")
def jobs_devops_local_search():
    return render_local_search_page()


@app.get("/jobs/devops/plot")
def view_plot():
    return jobs_devops_plot()


@app.post("/jobs/devops/notify")
def notify_users():
    df = devops_jobs_dataframe("devops", 50)
    return send_devops_jobs_update(df)


if __name__ == "__main__":
    app.run(debug=True)
