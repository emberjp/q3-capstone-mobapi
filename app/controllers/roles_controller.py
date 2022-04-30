from flask import jsonify
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session

from app.models import Role


def add_role():
    ...


def get_roles():
    query_role: Query = db.session.query(Role)

    role_query = query_role.order_by(Role.id).all()

    if not role_query:
        return {"err": "Nothing to list"}, 404

    return jsonify(role_query), 200


def edit_role(id):
    ...


def delete_role(id):
    ...
