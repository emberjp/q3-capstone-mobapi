from flask import jsonify, request
from app.configs.database import db
from app.models import Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from http import HTTPStatus


def add_game():
    game_data = request.get_json()
    new_game = Game(**game_data)
    db.session.add(new_game)
    db.session.commit()
    return jsonify(new_game), HTTPStatus.CREATED


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
