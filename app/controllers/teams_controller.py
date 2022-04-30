from http import HTTPStatus
from flask import jsonify
from app.configs.database import db
from app.models import Team, Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_team():
    ...


def get_teams(game):
    query_game: Query = db.session.query(Game)
    query_team: Query = db.session.query(Team)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    team_query = query_team.order_by(Team.id).all()

    if not team_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(team_query), 200


def get_team(game, id):
    query_game: Query = db.session.query(Game)
    query_team: Query = db.session.query(Team)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    team_query = query_team.filter_by(id=id).first()

    if not team_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(team_query), 200


def edit_team(id):
    ...


def delete_team(id):
    ...
