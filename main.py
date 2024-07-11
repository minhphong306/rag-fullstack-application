from flask import Flask
from flask import request
from index import initialize_index, get_index

app = Flask(__name__)
initialize_index()


@app.route("/")
def home():
    return "Hello World!"

@app.route("/query", methods=["GET"])
def query_index():
    query_text = request.args.get("text", None)
    if query_text is None:
        return (
            "No text found, please include a ?text=blah parameter in the URL",
            400,
        )
    index = get_index()
    query_engine = index.as_query_engine()
    response = query_engine.query(query_text)
    return str(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601)
