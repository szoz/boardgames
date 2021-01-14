from flask import Flask, jsonify, abort
from flask_cors import CORS

from static_bgs import bgs

app = Flask(__name__)
CORS(app)


@app.route('/')
def show_docs():
    return 'Available endpoint: /boardgames/'


@app.route('/boardgames')
def get_all_boardgames():
    return jsonify(bgs)


@app.route('/boardgames/<int:bg_id>')
def get_boardgame(bg_id):
    try:
        bg = bgs[bg_id]
        return jsonify(bg)
    except IndexError:
        return abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
