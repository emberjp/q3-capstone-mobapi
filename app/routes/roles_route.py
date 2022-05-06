from flask import Blueprint

from app.controllers import roles_controller

bp = Blueprint("roles", __name__, url_prefix="<string:game>/roles")

bp.post("")(roles_controller.add_role)
bp.get("")(roles_controller.get_roles)
bp.patch("/<int:id>")(roles_controller.edit_role)
bp.delete("/<int:id>")(roles_controller.delete_role)
