from flask import jsonify
from app.models import Position
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def add_position():
    ...


def get_positions():
    base_query: Query = db.session.query(Position)
    print(f"{base_query=}")
    positions = base_query.order_by(Position.id).all()

    
    return jsonify(positions), 200

def edit_position(id):
    ...


def delete_position(id):
    ...
