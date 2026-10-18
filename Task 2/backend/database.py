
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError


def save_submission(name, email, message):
    uri = os.getenv("MONGODB_URI")

    if not uri:
        raise RuntimeError("MONGODB_URI is not configured.")

    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=5000
    )

    try:
        client.admin.command("ping")

        database_name = os.getenv(
            "MONGODB_DATABASE",
            "flask_assignment"
        )

        collection = client[database_name]["submissions"]

        result = collection.insert_one({
            "name": name,
            "email": email,
            "message": message
        })

        return str(result.inserted_id)

    finally:
        client.close()
