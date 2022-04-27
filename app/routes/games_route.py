from flask import Blueprint

from app.controllers import games_controller

bp = Blueprint("games", __name__, url_prefix="/games")

bp.post("")(games_controller.add_game)
bp.get("")(games_controller.get_games)
bp.patch("/<int:id>")(games_controller.edit_game)
bp.delete("/<int:id>")(games_controller.delete_game)
