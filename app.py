from flask import Flask
import os

app = Flask(__name__)

# Point to the directory, not a specific file
DATA_PATH = "/app/data"

@app.route('/')
def index():
    content = "No data found on QNAP yet."
    
    if os.path.exists(DATA_PATH):
        # List all files in the directory
        files = os.listdir(DATA_PATH)
        if files:
            # Join the file names into a string for the webpage
            content = ", ".join(files)

    return f"""
    <h1>Nosxih DevOps Lab</h1>
    <p><b>Storage Status:</b> Reading from QNAP share...</p>
    <p><b>Content:</b> {content}</p>
    <p><i>Version: 1.1</i></p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
