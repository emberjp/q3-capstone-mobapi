from http import HTTPStatus
from app.configs.database import db
from app.models import Champion, Game
from flask import jsonify, request
from sqlalchemy import exc
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from http import HTTPStatus


def add_champion(game):
    champion_data = request.get_json()
    new_champion = Champion(**champion_data)
    champion_game = db.session.query(Game).filter_by(url_name=game.lower()).first()
    new_champion.game = champion_game
    db.session.add(new_champion)
    db.session.commit()
    return jsonify(new_champion), HTTPStatus.CREATED


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


def edit_champion(game, id):
    session: Session = db.session

    data = request.get_json()

    query_game = session.query(Game)
    query_champion = session.query(Champion)

    game_query = query_game.filter_by(url_name=game.lower()).first()

    if not game_query:
        return {"err": f"Game {game} not found"}, HTTPStatus.NOT_FOUND
    
    champion_query = query_champion.filter_by(id=id).first()

    if champion_query:
        for key, value in data.items():
        
            setattr(champion_query, key, value)
        
        session.commit()
        
        return jsonify(champion_query), HTTPStatus.OK

    else:
        
        return {'err': f"{id} doesn't exist"}, HTTPStatus.NOT_FOUND
    


def delete_champion(id):
    session: Session = db.session
    query_champion: Query = session.query(Champion)

    champion_query = query_champion.filter_by(id=id).first()

    if not champion_query:
        return {"err": "Not Found"}, 404

    session.delete(champion_query)
    session.commit()

    return jsonify(None), 204
