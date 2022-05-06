from flask import jsonify, request
from app.models import Position, Game
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from http import HTTPStatus


def add_position(game):
    position_data = request.get_json()
    new_position = Position(**position_data)
    position_game = db.session.query(Game).filter_by(url_name=game.lower()).first()
    new_position.game = position_game
    db.session.add(new_position)
    db.session.commit()
    return jsonify(new_position), HTTPStatus.CREATED


def get_positions(game):
    query_game: Query = db.session.query(Game)
    query_position: Query = db.session.query(Position)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    position_query = query_position.order_by(Position.id).all()

    if not position_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(position_query), 200


def edit_position(id):
    ...


def delete_position(id):
    ...
