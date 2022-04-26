from flask import Blueprint

from app.controllers import users_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.post("")(users_controller.add_category)
