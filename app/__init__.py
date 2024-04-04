from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config

from app.models.base import db

from typing import TYPE_CHECKING

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask("app")
    CORS(app)
    app.config.from_object(config_class)


    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.deadlines import bp as dead_bp
    app.register_blueprint(dead_bp)

    return app