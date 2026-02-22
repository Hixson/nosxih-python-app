from flask import Flask
import os

app = Flask(__name__)

# Point to the directory, not a specific file
DATA_PATH = "/app/data"

@app.route('/')
def index():
    content = "No data found on QNAP yet."
    version = os.getenv('APP_VERSION', 'local-dev')
    if os.path.exists(DATA_PATH):
        # List all files in the directory
        files = os.listdir(DATA_PATH)
        if files:
            # Join the file names into a string for the webpage
            content = ", ".join(files)

    return f"""
    <h1>Nosxih DevOps Lab</h1>
    <h1>DevOps Lab v1.1</h1><p>Running version: {version}</p>
    <p><b>Storage Status:</b> Reading from QNAP share...</p>
    <p><b>Content:</b> {content}</p>
    """

@app.route('/test')
def test():
    return f"Now is the time for all good men to come to the aid of their country."

@app.route('/health')
def health():
    # You could add logic here to check if the QNAP mount is reachable
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
