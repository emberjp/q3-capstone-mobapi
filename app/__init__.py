from flask import Flask

from app.configs import database, migration
from app import routes


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def invalid_rourte(e):
        return {"err": "Route not found"}, 404

    @app.errorhandler(405)
    def invalid_rourte(e):
        return {"err": "Route not found"}, 404

    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)

    return app
