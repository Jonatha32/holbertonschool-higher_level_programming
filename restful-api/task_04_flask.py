from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


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

    if not data.get('username'):
        return (jsonify({"error": "Username is required"}), 400)

    users[data['username']] = data
    return (jsonify({"message": "User add", "user": data}), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
