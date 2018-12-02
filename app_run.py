# from app1 import flask_app_var
import app1
# from app1.views import views_bp
# bps = [views_bp,]
from app1 import auth
bp_list = [auth.bp,]
app = app1.create_app(blue_print_list=bp_list)