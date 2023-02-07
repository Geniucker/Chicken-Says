import flask
import encode
import decode
from gevent import pywsgi


app = flask.Flask(__name__)

@app.route("/encode", methods=["POST", "GET"])
def encodePage():
    args = flask.request.values
    original = args.get("q")
    headers = {
        "Content-Type": "text/plain;charset=utf-8"
    }
    return encode.encode(original), headers


@app.route("/decode", methods=["POST", "GET"])
def decodePage():
    args = flask.request.values
    original = args.get("q")
    headers = {
        "Content-Type": "text/plain;charset=utf-8"
    }
    return decode.decode(original), headers


@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")


if __name__ == "__main__":
    # Debug
    # app.run(host="0.0.0.0", port=443, debug=True)
    # Production
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    server.serve_forever()
