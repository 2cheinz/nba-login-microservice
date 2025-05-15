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