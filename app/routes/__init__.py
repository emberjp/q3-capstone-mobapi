from flask import Blueprint, Flask

from .champions_route import bp as bp_champions
from .games_route import bp as bp_games
from .positions_route import bp as bp_positions
from .roles_route import bp as bp_roles
from .teams_route import bp as bp_teams
from .users_route import bp as bp_users

bp_api = Blueprint("api", __name__, url_prefix="")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_champions)
    bp_api.register_blueprint(bp_games)
    bp_api.register_blueprint(bp_positions)
    bp_api.register_blueprint(bp_roles)
    bp_api.register_blueprint(bp_teams)
    bp_api.register_blueprint(bp_users)

    app.register_blueprint(bp_api)
