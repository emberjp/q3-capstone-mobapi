from flask import Blueprint

from app.controllers import users_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.post("")(users_controller.add_user)
bp.get("")(users_controller.get_users)
bp.patch("/<int:id>")(users_controller.edit_user)
bp.delete("/<int:id>")(users_controller.delete_user)
