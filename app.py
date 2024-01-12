from flask import Flask
import time


app = Flask(__name__)

@app.route("/")
def hello_world():
    time.sleep(30)
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run('0.0.0.0')