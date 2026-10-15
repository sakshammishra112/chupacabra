from flask import Blueprint, jsonify, request

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    return jsonify(message="Hello, DevOps!")


@main_bp.get("/health")
def health():
    return jsonify(status="ok")


@main_bp.get("/greet/<name>")
def greet(name: str):
    return jsonify(message=f"Hello, {name}!")


@main_bp.get("/add")
def add():
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")

    try:
        a = float(a_raw)
        b = float(b_raw)
    except (TypeError, ValueError):
        return jsonify(error="query params 'a' and 'b' must both be numbers"), 400

    return jsonify(result=a + b)
