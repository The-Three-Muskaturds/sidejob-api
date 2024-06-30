from flask import Blueprint, current_app, request, jsonify
from flask_cors import cross_origin
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


class ErrorMessages:
    MISSING_FIELDS = "All fields are required."
    INVALID_DATA_FORMAT = "Invalid data format."
    USER_EXISTS = "User already exists."
    SUCCESS = "User registered successfully."


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    missing_fields = [
        field
        for field in ["first_name", "last_name", "username", "email", "password"]
        if not data.get(field)
    ]
    if missing_fields:
        return jsonify(
            {
                "error": "Missing fields",
                "message": ErrorMessages.MISSING_FIELDS,
                "missing_fields": missing_fields,
            }
        ), 400

    invalid_fields = [
        field
        for field in [first_name, last_name, username, email, password]
        if not isinstance(field, str)
    ]
    if invalid_fields:
        return jsonify(
            {
                "error": "Invalid data format",
                "message": ErrorMessages.INVALID_DATA_FORMAT,
                "invalid_fields": invalid_fields,
            }
        ), 400

    if auth_service.register_user(first_name, last_name, username, email, password):
        return jsonify({"message": ErrorMessages.SUCCESS}), 200
    else:
        return jsonify(
            {"error": "User already exists", "message": ErrorMessages.USER_EXISTS}
        ), 400


@auth_bp.route("/login", methods=["POST"])
@cross_origin(origins=["http://localhost:3000"], supports_credentials=True)
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    access_token, refresh_token = auth_service.authenticate_user(username, password)
    if access_token and refresh_token:
        response = jsonify({"msg": "Login successful"})
        response.set_cookie(
            "access_token_cookie",
            access_token,
            secure=False,
            httponly=True,
            samesite="Lax",
            path="/",
        )
        response.set_cookie(
            "refresh_token_cookie",
            refresh_token,
            secure=False,
            httponly=True,
            samesite="Lax",
            path="/",
        )
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
