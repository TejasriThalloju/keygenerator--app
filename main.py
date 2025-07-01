from flask import Flask, jsonify
from key_generator import get_secret_key
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/secret-key")
def get_key():
    secret = get_secret_key()
    return jsonify({"SECRET_KEY": secret})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
