
from flask import Blueprint, render_template

frontend_bp = Blueprint("frontend", __name__)


@frontend_bp.route("/")
def home():
    return render_template(
        "index.html",
        error=None,
        form_data={}
    )


@frontend_bp.route("/success")
def success():
    return render_template("success.html")
