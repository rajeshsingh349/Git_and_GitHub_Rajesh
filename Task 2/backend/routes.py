
from flask import Blueprint, render_template, request, redirect, url_for
from pymongo.errors import PyMongoError

from backend.database import save_submission

backend_bp = Blueprint("backend", __name__)


@backend_bp.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    form_data = {
        "name": name,
        "email": email,
        "message": message
    }

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="Please fill in all fields.",
            form_data=form_data
        ), 400

    try:
        save_submission(name, email, message)

        return redirect(url_for("frontend.success"))

    except (PyMongoError, RuntimeError, Exception) as error:
        return render_template(
            "index.html",
            error=f"Submission failed: {error}",
            form_data=form_data
        ), 500
