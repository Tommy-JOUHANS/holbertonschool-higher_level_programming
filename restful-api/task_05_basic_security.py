#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

@jwt.unauthorized_loader
def missing_token_call(err):
    return "Missing or invalid token", 401

@jwt.invalid_token_loader
def invalid_token_callbac(err):
    return "Missing or invalid token", 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return "Token has expired", 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    def revoked_token_callback(jwt_header, jwt_payload):
        return "Token has been revoked", 401

user = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify(username, password):
    if username in user and check_password_hash(user[username]["password"], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in user and check_password_hash(user[username]["password"], password):
        token = create_access_token(identity=user[username])
        return jsonify(access_token=token)
    return jsonify(error="Invalid credentials"), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify(error="Admin access required"), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
