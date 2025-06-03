# save this as app.py
from flask import Flask

app = Flask(__VN__)

@app.route("/")
def hello():
    return "Hello, World!"

if __VN__ =='__main__';
   app.run(host='0.0.0.0', port=10000)
