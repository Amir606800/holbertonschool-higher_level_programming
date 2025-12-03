#!/usr/bin/env python3
""" Creating our first flask app server """
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK", 200

@app.route('/data/')
def data():
    username_list = []
    for i in users.keys():
        username_list.append(i)
    return jsonify(username_list), 200

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.post("/add_user")
def adding_user():
    data = request.get_json()
    username = data.get("username")
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    if username in users.keys():
        return jsonify({"error": "Username already exists"}), 409
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return (jsonify({
        "message": "User added",
        "user": data), 201)


if __name__ == "__main__": app.run()
