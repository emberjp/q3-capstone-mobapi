from http import HTTPStatus
from flask import jsonify, request
from app.configs.database import db
from app.models import Team, Game
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_team(game):
    try:
        team_data = request.get_json()
        new_team = Team(**team_data)
        team_game = db.session.query(Game).filter_by(url_name=game.lower()).first()
        new_team.game = team_game
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team), HTTPStatus.CREATED
    except AttributeError:
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


def data_to_edit(query, data):
    for key, value in data.items():
        setattr(query, key, value)
    
    return query


def edit_team(game, id):
    query_game: Query = db.session.query(Game)
    query_team: Query = db.session.query(Team)
    game_query = query_game.filter_by(url_name=game.lower()).first()
    data = request.get_json()

    if not game_query:
        return {"err": f"Game {game} not found"}, 404

    team_query = query_team.filter_by(id=id).first()
    data_to_edit(team_query, data)

    if not team_query:
        return {"err": "Nothing to edit"}, 404

    return jsonify(team_query), 200


def delete_team(id):
    query_team: Query = db.session.query(Team)

    team_query = query_team.filter_by(id=id).first()

    if not team_query:
        return {"err": "Not Found"}, 404

    db.session.delete(team_query)
    db.session.commit()

    return jsonify(None), 204
