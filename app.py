from flask import Flask
# test
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
