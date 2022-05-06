from flask import jsonify, request
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from http import HTTPStatus
from app.models import Role


def add_role(game):
    role_data = request.get_json()
    new_role = Role(**role_data)
    db.session.add(new_role)
    db.session.commit()
    return jsonify(new_role), HTTPStatus.CREATED


def get_roles(game):
    query_role: Query = db.session.query(Role)

    role_query = query_role.order_by(Role.id).all()

    if not role_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(role_query), 200


def edit_role(id):
    ...


def delete_role(id):
    ...
