from flask import Blueprint, request, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

@api_bp.route("/greet/<name>", methods=["GET"])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})
