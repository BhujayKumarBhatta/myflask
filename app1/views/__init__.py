from flask import Blueprint

views_bp = Blueprint('views', __name__) 
from app1.views import routes  