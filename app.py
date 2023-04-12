from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_allowed_user(username):
    with open("allowed_users.txt", "r") as file:
        allowed_users = [line.strip() for line in file.readlines()]
    return username in allowed_users

@app.route('/api/login', methods=['GET'])
def login():
    username = request.args.get('username')
    if is_allowed_user(username):
        return jsonify({"allowed": True})
    else:
        return jsonify({"allowed": False})

if __name__ == "__main__":
    app.run(debug=True)
