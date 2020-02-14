from flask import Blueprint

bp = Blueprint('loglist', __name__, url_prefix='/loglist')

from app.loglist import routes
