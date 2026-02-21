from flask import Flask
import os

app = Flask(__name__)

# This path will be where we mount your QNAP share in Kubernetes
DATA_PATH = "/app/data/test.txt"

@app.route('/')
def index():
    content = "No data found on QNAP yet."
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            content = f.read()
    
    return f"""
    <h1>Nosxih DevOps Lab</h1>
    <p><b>Storage Status:</b> Reading from QNAP share...</p>
    <p><b>Content:</b> {content}</p>
    <p><i>Version: 1.0</i></p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
