from flask import jsonify
from app.configs.database import db
from app.models import Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_game():
    ...


def get_games():
    query_game: Query = db.session.query(Game)
    game_query = query_game.order_by(Game.id).all()

    if not game_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(game_query), 200


def edit_game(id):
    ...


def delete_game(id):
    ...
