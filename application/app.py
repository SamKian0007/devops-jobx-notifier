from flask import Flask, render_template, session
from dotenv import load_dotenv
import os

from application.jobs_dataframe import devops_jobs_dataframe
from application.dataframe_plot import jobs_devops_plot
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



@app.get("/jobs/devops")
def jobs_devops():
    df = devops_jobs_dataframe("devops", 50)
    return f"<h2>DevOps Jobs</h2>{df.to_html(index=False, border=1)}"


@app.get("/jobs/devops/plot")
def _view_plot():
    return jobs_devops_plot()


@app.post("/jobs/devops/notify")
def notify_users():
    df = devops_jobs_dataframe("devops", 50)
    return send_devops_jobs_update(df)


if __name__ == "__main__":
    app.run(debug=True)
