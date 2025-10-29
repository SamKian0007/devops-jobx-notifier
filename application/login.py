import os
from flask import Blueprint, request, redirect, url_for, flash, session, render_template
from dotenv import load_dotenv
load_dotenv()  # keep as-is

ENV_USER = os.getenv("APP_USERNAME", "")
ENV_PASS = os.getenv("APP_PASSWORD", "")

bp = Blueprint("auth", __name__)


@bp.get("/login")
def login_form():
    return render_template("login")

@bp.post("/login")
def login():
    u = request.form.get("username", "")
    p = request.form.get("password", "")
    if u == ENV_USER and p == ENV_PASS:
        session["logged_in"] = True
        session["username"] = u
        flash("Logged in successfully.", "success")
        return redirect(url_for("home"))
    else:
        flash("Invalid username or password. Please try again.", "error")
        return redirect(url_for("retry_login"))                    

@bp.get("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("username", None)
    flash("Logged out.", "info")
    return redirect(url_for("home"))
