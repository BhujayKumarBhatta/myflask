# from app1 import flask_app_var
import os
import konfig
import app1
# from app1.views import views_bp
# bps = [views_bp,]
from app1 import auth
from app1.views import views_bp
from app1.authentication.check_req_obj import req_obj_bp
from app1.authentication.tokenops import token_bp

_HERE = os.path.dirname(__file__)
_SETTINGS_FILE = os.path.join(_HERE, 'settings.ini')

CONFS = konfig.Config(_SETTINGS_FILE)
flask_default_setiings_map = CONFS.get_map('flask_default')
token_settings_map = CONFS.get_map('token')
prod_configs = [flask_default_setiings_map,
                        token_settings_map,]


bp_list = [auth.bp,views_bp, req_obj_bp,token_bp]

app = app1.create_app(config_map_list= prod_configs,
                      blue_print_list=bp_list)