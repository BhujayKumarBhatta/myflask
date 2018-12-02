from flask import Flask

# flask_app_var = Flask(__name__)

# def create_app(config_file=None, app_blueprints=[]):
#     app = Flask(__name__) 
#     #for bp in app_blueprints: 
#     from app1.views import views_bp   
#     app.register_blueprint(views_bp)          
#     return app


# from app1.views import views_bp
# flask_app_var.register_blueprint(views_bp)


def create_app(config_file=None, blue_print_list=[]):
    app = Flask(__name__)
    for bp in blue_print_list:
        app.register_blueprint(bp)
    return app
