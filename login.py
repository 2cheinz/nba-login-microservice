from flask import Flask, request, jsonify
import json
import os
import secrets

app = Flask(__name__)

DATA_FILE = 'user_info.json'
user_tokens = {}

# generate token for returning, using token_hex method per docs.python.org
def generate_token():
    return secrets.token_hex(16)


# get existing users
# using json decodeerror per json parsing errors in python on geeks for geeks
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as user_file:
        try:
            user_tokens = json.load(user_file)
        except json.JSONDecodeError:
            print("Invalid JSON, error, please try again!")
            user_tokens = {}    # setting this as empty in case json errors out

# save tokens to file
def save_tokens():
    with open(DATA_FILE, 'w') as user_file:
        json.dump(user_tokens, user_file, indent=2)

# login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')

    token = generate_token()
    user_tokens[username] = token
    save_tokens()

    return jsonify({'token': token})


# validate route
@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    token = data.get('token')

    valid_token = token in user_tokens.values()
    return jsonify({'valid': valid_token})

# run this on port 5001
if __name__ == '__main__':
    app.run(port=5001)