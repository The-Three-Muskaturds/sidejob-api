from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity,
)
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()


@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    if auth_service.register_user(username, password):
        return jsonify({"msg": "User registered successfully"}), 200
    return jsonify({"msg": "User already exists"}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    access_token, refresh_token = auth_service.authenticate_user(username, password)
    if access_token and refresh_token:
        response = jsonify({"msg": "Login successful"})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    return jsonify({"msg": "Bad username or password"}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"logged_in_as": current_user}), 200


@auth_bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    response = jsonify({"msg": "Token refreshed"})
    set_access_cookies(response, access_token)
    return response
