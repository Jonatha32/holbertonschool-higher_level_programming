from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, verify_jwt_in_request
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"   
    },
    "admin": {
        "username": "admin",
        "password": generate_password_hash("admin"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error(status):
    return jsonify({'error': 'Unauthorized access'}), status

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usern = data.get('username')
    pw = data.get('password')
    
    if not usern or not pw:
        return jsonify({"error": "Missing username or password"}), 400
    if usern not in users or not check_password_hash(users[usern]['password'], pw):
        return jsonify({"error": "Invalid username or password"}), 401
    access_tok = create_access_token(
        identity={'username': usern, 'role': users[usern]['role']},
    )
    return jsonify({
        "access_tok" : access_tok
        })

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access granted"})

@app.route('/admin-only', methods=['GET'])
def admin_only():
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin access granted"})

if __name__ == '__main__':
    app.run(debug=True)