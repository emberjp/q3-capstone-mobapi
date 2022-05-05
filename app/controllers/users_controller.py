from flask import jsonify, request
from app.configs.database import db
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from http import HTTPStatus

from app.models import Game, User


def add_user(game):
    try:
        user_data = request.get_json()
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), HTTPStatus.CREATED
    except exc.IntegrityError:
        return {"err": "this email is already in use"}, HTTPStatus.CONFLICT
    
    except exc.DataError:
        return {"err": "name or email value is too large: name must be a maximum of 20 characters and email must be 50 characters"}, HTTPStatus.CONFLICT


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


def edit_user(game, id):
    session: Session = db.session

    data = request.get_json()

    query_game = session.query(Game)
    query_user = session.query(User)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, HTTPStatus.NOT_FOUND

    user_query = query_user.filter_by(id=id).first()

    if user_query:
        for key, value in data.items():

            setattr(user_query, key, value)

        session.commit()

        return jsonify(user_query), HTTPStatus.OK

    else:

        return {"err": f"Id {id} doesn't exist"}, HTTPStatus.NOT_FOUND


def delete_user(game, id):
    session: Session = db.session()

    query_game = session.query(Game)
    query_user = session.query(User)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, HTTPStatus.NOT_FOUND

    user_query = query_user.filter_by(id=id).first()

    if user_query:
        session.delete(user_query)

        session.commit()

        return "", HTTPStatus.NO_CONTENT
    else:
        return {"error": f" Id {id} doesn't exists"}, HTTPStatus.NOT_FOUND
