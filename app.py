from flask import Flask

app = Flask(__name__)


@app.route("/")  # what url to trigger when hello() is called
def hello():
    return "Working!"


if __name__ == "__main__":
    app.run(debug=True, port=23145)
