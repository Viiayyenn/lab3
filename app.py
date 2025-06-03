
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return template('index.html')

if __name__ == '__main__':
    # Chạy ở chế độ debug để dễ phát triển
    app.run(host='0.0.0.0', port=5000, debug=True)
