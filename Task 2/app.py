"""
Task 2: Frontend Form with MongoDB Atlas
- Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
- On success: the user should be redirected to another page displaying the message “Data submitted successfully”.
- On error: display the error on the same page without redirection.
"""
from flask import Flask
from dotenv import load_dotenv
from backend.routes import backend_bp
from frontend.routes import frontend_bp

load_dotenv()

app = Flask(
    __name__,
    template_folder="frontend/templates"
)

app.register_blueprint(frontend_bp)
app.register_blueprint(backend_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
