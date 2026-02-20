#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

basic_auth = HTTPBasicAuth()

users_basic = {}

@basic_auth.verify_password
def verify_basic(username, password):
    if username in users_basic and check_password_hash(users_basic[username], password):
        return username
    return None

@app.route("/basic-protected")
@basic_auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

users_jwt = {}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users_jwt.get(username)
    if user and user["password"] == password:
        token = create_access_token(identity=username)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    user = get_jwt_identity()
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    roles = users_jwt[user]["roles"]
    if "admin" not in roles:
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(debug=True)