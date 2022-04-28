from flask import jsonify
from app.configs.database import db
from app.models import Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_game():
    ...


def get_games():
    base_query: Query = db.session.query(Game)
    print(f"{base_query=}")
    games = base_query.order_by(Game.id).all()

    return jsonify(games), 200


def edit_game(id):
    ...


def delete_game(id):
    ...
