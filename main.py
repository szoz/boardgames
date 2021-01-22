from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

from models import Game

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def show_docs():
    """Main page, returns string with available endpoints."""
    return 'Available endpoint: /boardgames, /boardgames/<id>'


@app.route('/boardgames')
def get_all_boardgames():
    """Return list of dicts with all boardgames data."""
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)
    games_paginated = Game.query.order_by(Game.id).paginate(page=page, per_page=limit)

    payload = [game.to_dict() for game in games_paginated.items]
    for game in payload:
        game['rank'] = game['id']  # to be replaced with calculating rate based on users score

    response = jsonify(payload)
    response.headers['X-Total-Count'] = games_paginated.total
    return response


@app.route('/boardgames/<int:bg_id>')
def get_boardgame(bg_id):
    """Return dict with boardgame data based on given id."""
    game = Game.query.filter_by(id=bg_id).first_or_404()
    payload = game.to_dict()
    payload['rank'] = payload['id']  # to be replaced with calculating rate based on users score
    return jsonify(payload)
