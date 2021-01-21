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
    query_bgs = [game.to_dict() for game in Game.query.all()]
    return jsonify(query_bgs)


@app.route('/boardgames/<int:bg_id>')
def get_boardgame(bg_id):
    """Return dict with boardgame data based on given id."""
    game = Game.query.filter_by(id=bg_id).first_or_404()
    return jsonify(game.to_dict())
