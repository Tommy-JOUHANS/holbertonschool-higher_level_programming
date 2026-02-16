#!/usr/bin/python3
"""Module that implements
a simple RESTful API using Flask,
 a popular web framework for Python.

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
    "username": "jane",
    "name": "Jane",
    "age": 28,
    "city": "Los Angeles"
   },
"john": {
    "username": "john",
    "name": "John",
    "age": 30,
    "city": "New York"
   }
}


@app.route("/", methods=["GET"])
def home():
    """Handle GET requests to the root URL."""
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """Handle GET requests to the /data URL."""
    return jsonify(list(users.keys())), 200



@app.route("/status", methods=["GET"])
def status():
    """Handle GET requests to the /status URL."""
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Handle GET requests to the /users/<username> URL."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200



@app.route("/add_user", methods=["POST"])
def add_user():

    data = request.get_json()


    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
