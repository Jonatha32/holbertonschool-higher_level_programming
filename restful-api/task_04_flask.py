from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return ("OK")


@app.route('/users/<username>')
def get_user(username):
    user_ = users.get(username)
    if user_:
        return jsonify(user_)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not isinstance(data, dict):
        return (jsonify({"error": "Invalid JSON format"}), 400)

    user_name = data.get("username", "").strip()
    if not user_name:
        return (jsonify({"error": "Username is required"}), 400)

    if user_name == users:
        return (jsonify({"error": "User already exists"}), 400)

    users[user_name] = {
        "username": user_name,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return (jsonify({"message": "User added", "user": users[user_name]}), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
