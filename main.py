from flask import Flask
from index import initialize_index

app = Flask(__name__)
initialize_index()


@app.route("/")
def home():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601)
