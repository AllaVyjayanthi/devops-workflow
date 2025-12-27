import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "environment": os.getenv("ENV"),
        "debug": os.getenv("DEBUG"),
        "log_level": os.getenv("LOG_LEVEL"),
        "database": os.getenv("DB_URL")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
