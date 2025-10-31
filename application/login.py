# login.py
"""Module defining the authentication blueprint.

This module manages user login and logout actions using environment-based
credentials. It handles session creation, validation, and cleanup for
authenticated users.
"""

import os
from flask import Blueprint, request, redirect, url_for, flash, session
from dotenv import load_dotenv

load_dotenv()

ENV_USER = os.getenv("APP_USERNAME", "")
ENV_PASS = os.getenv("APP_PASSWORD", "")

bp = Blueprint("auth", __name__)


@bp.post("/login")
def login():
    """Handle user login and session creation."""
    u = request.form.get("username", "")
    p = request.form.get("password", "")
    if u == ENV_USER and p == ENV_PASS:
        session["logged_in"] = True
        session["username"] = u
        flash("Logged in successfully.", "success")
        return redirect(url_for("login"))
    flash("Invalid username or password.", "error")
    return redirect(url_for("home"))


@bp.get("/logout")
def logout():
    """Handle user logout and session cleanup."""
    session.pop("logged_in", None)
    session.pop("username", None)
    flash("Logged out.", "info")
    return redirect(url_for("home"))
