from flask import Blueprint

bp = Blueprint("deadlines", __name__)

from app.routes.deadlines import routes