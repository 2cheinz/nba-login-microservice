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

