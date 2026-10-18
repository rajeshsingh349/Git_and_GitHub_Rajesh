"""
Task 1: JSON API Route
Created sample list inside data/api_data.json as backend file. 
"""
import json
from pathlib import Path
from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "api_data.json"
)


@app.route("/api")
def get_api_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return jsonify({"error": "Expected a JSON list"}), 500

        return jsonify(data)

    except (OSError, json.JSONDecodeError) as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(port=5001, debug=True)
