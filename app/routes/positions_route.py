from flask import Blueprint

from app.controllers import positions_controller

bp = Blueprint("positions", __name__, url_prefix="/positions")

bp.post("")(positions_controller.add_position)
bp.get("")(positions_controller.get_positions)
bp.patch("/<int:id>")(positions_controller.edit_position)
bp.delete("/<int:id>")(positions_controller.delete_position)
