# from app1 import flask_app_var
import app1
# from app1.views import views_bp
# bps = [views_bp,]
from app1 import auth
from app1.views import views_bp
from app1.authentication.check_req_obj import req_obj_bp
bp_list = [auth.bp,views_bp, req_obj_bp]
app = app1.create_app(blue_print_list=bp_list)