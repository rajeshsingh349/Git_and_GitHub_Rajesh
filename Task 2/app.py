"""
Task 2: Frontend Form with MongoDB Atlas for To-Do Items
- Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
- On success: the user should be redirected to another page displaying the message “Data submitted successfully”.
- On error: display the error on the same page without redirection.
"""
from flask import Flask, jsonify, render_template,request
from dotenv import load_dotenv
from backend.routes import backend_bp
from frontend.routes import frontend_bp
from pymongo.errors import PyMongoError
from backend.database import mongo_client, todo_collection

load_dotenv()

app = Flask(
    __name__,
    template_folder="frontend/templates"
)

app.register_blueprint(frontend_bp)
app.register_blueprint(backend_bp)

@app.route("/todo")
def todo():
    return render_template("todo.html")
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON request body is required"}), 400

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not isinstance(item_name, str) or not item_name.strip():
        return jsonify({"error": "itemName is required"}), 400

    if (
        not isinstance(item_description, str)
        or not item_description.strip()
    ):
        return jsonify({"error": "itemDescription is required"}), 400

    try:
        mongo_client.admin.command("ping")

        result = todo_collection.insert_one({
            "itemName": item_name.strip(),
            "itemDescription": item_description.strip()
        })

        return jsonify({
            "message": "To-Do item saved successfully",
            "id": str(result.inserted_id)
        }), 201

    except PyMongoError:
        app.logger.exception("MongoDB operation failed")
        return jsonify({"error": "Database operation failed"}), 500
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
