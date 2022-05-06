from flask import Blueprint

from app.controllers import champions_controller

bp = Blueprint("champions", __name__, url_prefix="/<string:game>/champions")

bp.post("")(champions_controller.add_champion)
bp.get("")(champions_controller.get_champions)
bp.patch("/<int:id>")(champions_controller.edit_champion)
bp.delete("/<int:id>")(champions_controller.delete_champion)
