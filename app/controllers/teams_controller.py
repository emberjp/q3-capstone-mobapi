from http import HTTPStatus
from flask import jsonify, request
from app.configs.database import db
from app.models import Team, Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_team():
    try:
        team_data = request.get_json()
        new_team = Team(**team_data)
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team), HTTPStatus.CREATED
    except exc.IntegrityError:
        return {
            "error": 409,
            "message": "There is already a team with this name",
        }, HTTPStatus.CONFLICT


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


def get_team(id):
    base_query: Query = db.session.query(Team)
    team = base_query.filter(Team.id == id).first()

    if team:
        return jsonify(team), HTTPStatus.OK

    return {"err": f"team {id} does not exist"}, HTTPStatus.NOT_FOUND


def edit_team(id):
    ...


def delete_team(id):
    ...
