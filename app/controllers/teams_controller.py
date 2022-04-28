from flask import jsonify
from app.configs.database import db
from app.models import Team
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_team():
    ...


def get_teams():
    base_query: Query = db.session.query(Team)
    teams = base_query.order_by(Team.id).all()

    return jsonify(teams), 200


def get_team(id):
    ...


def edit_team(id):
    ...


def delete_team(id):
    ...
