from flask import Blueprint

from app.controllers import teams_controller

bp = Blueprint("teams", __name__, url_prefix="/<string:game>/teams")

bp.post("")(teams_controller.add_team)
bp.get("")(teams_controller.get_teams)
bp.get("<int:id>")(teams_controller.get_team)
bp.patch("/<int:id>")(teams_controller.edit_team)
bp.delete("/<int:id>")(teams_controller.delete_team)
