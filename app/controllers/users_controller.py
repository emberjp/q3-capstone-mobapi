from flask import jsonify
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session

from app.models import Game, User


def add_user():
    ...


def get_users(game):
    query_user: Query = db.session.query(User)
    query_game: Query = db.session.query(Game)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    user_query = query_user.order_by(User.id).all()

    if not user_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(user_query), 200


def edit_user(id):
    ...


def delete_user(id):
    ...
