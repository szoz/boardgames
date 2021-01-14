from flask import Flask, jsonify, abort

from static_bgs import bgs

app = Flask(__name__)


@app.route('/')
def show_docs():
    return 'Available endpoint: /boardgames/'


@app.route('/boardgames')
def get_all_boardgames():
    response = jsonify(bgs)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/boardgames/<int:bg_id>')
def get_boardgame(bg_id):
    try:
        bg = bgs[bg_id]
        response = jsonify(bg)
    except IndexError:
        response = abort(404)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
