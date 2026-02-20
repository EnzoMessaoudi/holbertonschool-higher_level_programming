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

roles_basic = {}

@basic_auth.verify_password
def verify_password(username, password):
    if username in users_basic and check_password_hash(users_basic[username], password):
        return username
    return None

@basic_auth.get_user_roles
def get_roles(username):
    return roles_basic.get(username, [])

users_jwt = {}

@app.route("/basic")
@basic_auth.login_required
def basic_protected():
    user = basic_auth.current_user()
    return jsonify({"message": f"Hello {user}, you passed Basic Auth!"})

@app.route("/basic-admin")
@basic_auth.login_required(role="admin")
def basic_admin():
    user = basic_auth.current_user()
    return jsonify({"message": f"Hello {user}, you are an admin!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users_jwt and users_jwt[username]["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    user = get_jwt_identity()
    return jsonify({"message": f"Hello {user}, you passed JWT Auth!"})

@app.route("/jwt-admin")
@jwt_required()
def jwt_admin():
    user = get_jwt_identity()
    roles = users_jwt[user]["roles"]
    if "admin" not in roles:
        return jsonify({"msg": "Admins only!"}), 403
    return jsonify({"message": f"Hello {user}, you are an admin!"})

if __name__ == "__main__":
    app.run(debug=True)