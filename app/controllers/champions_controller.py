from app.configs.database import db
from app.models import Champion, Game
from flask import jsonify
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_champion(game):
    ...


def get_champions(game):
    query_champion: Query = db.session.query(Champion)
    query_game: Query = db.session.query(Game)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    champion_query = query_champion.order_by(Champion.id).all()

    if not champion_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(champion_query), 200


def edit_champion(id):
    ...


def delete_champion(id):
    ...
