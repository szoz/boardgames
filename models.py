from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

db = SQLAlchemy()


class SerializeMixin:

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


class Game(db.Model, SerializeMixin):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brief = db.Column(db.String)
    score = db.Column(db.Float)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    categories = db.Column(ARRAY(db.String))
    complexity = db.Column(db.Float)

    def __repr__(self):
        return f'<Game: {self.name}>'
