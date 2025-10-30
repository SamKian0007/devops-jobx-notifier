from flask import Flask, render_template, session, url_for, redirect, request
from dotenv import load_dotenv
import os

from application.jobs_dataframe import devops_jobs_dataframe
from application.dataframe_plot import jobs_devops_plot
from application.dataframe_devops import jobs_devops_formated
from application.notify import send_devops_jobs_update
from application.login import bp as auth_bp  # NEW

load_dotenv()

app = Flask(__name__)
# needed for session/flash
app.secret_key = os.getenv("SECRET_KEY", "change-me")
app.register_blueprint(auth_bp)  # NEW


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/login")
def login():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("login.html", title="login", header="Job Explorer !")


@app.post("/jobs/filter")
def jobs_filter_post():
    # Collect form data
    user_posts = request.form.to_dict(flat=True)
    params = get_params_from_user_posts(user_posts)
    results = []
    try:
        results = fetch_jobs_with_filters(params)
    except Exception as e:
        # Minimal error handling: show empty results; in a fuller app, use flash/alerts
        results = []
    return render_template(
        "jobs_filter.html",
        title="Job Filter",
        header="Filter Jobs",
        results=results,
        params=params,
    )


@app.get("/jobs/devops")
def jobs_devops():
    keyword = request.args.get("keyword", "devops")
    return jobs_devops_formated(keyword)


@app.get("/jobs/devops/plot")
def view_plot():
    return jobs_devops_plot()


@app.post("/jobs/devops/notify")
def notify_users():
    df = devops_jobs_dataframe("devops", 50)
    return send_devops_jobs_update(df)


if __name__ == "__main__":
    app.run(debug=True)
