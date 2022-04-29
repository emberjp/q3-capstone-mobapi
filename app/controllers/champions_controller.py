from app.configs.database import db
from app.models import Champion
from flask import jsonify
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session

from app.models.games_model import Game


def add_champion():
    ...


def get_champions(game):
    query_champions: Query = db.session.query(Champion)
    query_game: Query = db.session.query(Game)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    print(f"{game_query=}")

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    champions_query = query_champions.order_by(Champion.id).all()

    if not champions_query:
        return {"err": "No champions to list"}, 404

    return jsonify(champions_query), 200


def edit_champion(id):
    ...


def delete_champion(id):
    ...
