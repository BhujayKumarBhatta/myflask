from flask import Blueprint

bp = Blueprint('auth', __name__)

@bp.route('/')
def hello():
    return 'Hello Flask'