# save this as app.py
from flask import Flask

app = Flask(__VN__)

@app.route("/")
def hello():
    return "Hello, World!"
