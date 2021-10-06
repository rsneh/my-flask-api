from flask import Flask, jsonify, request
from my_api.database.users import get_users, get_user, add_user, delete_user

app = Flask(__name__)

# REST API


# Get all users
@app.route("/users",  methods=['GET'])
def users_api():
    users = get_users()
    return jsonify(users)

# Get one user by id


@app.route("/users/<id>", methods=['GET'])
def users_get_one_api(id):
    user = get_user(id)
    return jsonify(user)


@app.route("/users", methods=['POST'])
def users_create_api():
    new_user = request.get_json()
    added_user = add_user(new_user)
    return added_user


@app.route("/users/<id>", methods=['DELETE'])
def users_delete_api(id):
    user = delete_user(id)
    return jsonify(user)
