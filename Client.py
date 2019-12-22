import hashlib
import random
import time
import requests
from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return str(open("static/Client.html").read()),200


if __name__ == "__main__":
    app.run(debug=True, port=80)
