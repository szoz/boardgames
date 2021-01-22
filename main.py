from flask import Flask, jsonify
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
    games_dict = [game.to_dict() for game in Game.query.order_by(Game.id)]
    for game in games_dict:
        game['rank'] = game['id']  # to be replaced with calculating rate based on users score
    return jsonify(games_dict)


@app.route('/boardgames/<int:bg_id>')
def get_boardgame(bg_id):
    """Return dict with boardgame data based on given id."""
    game = Game.query.filter_by(id=bg_id).first_or_404()
    game_dict = game.to_dict()
    game_dict['rank'] = game_dict['id']  # to be replaced with calculating rate based on users score
    return jsonify(game_dict)
