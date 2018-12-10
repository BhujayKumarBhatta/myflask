from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# flask_app_var = Flask(__name__)

# from app1.views import views_bp
# flask_app_var.register_blueprint(views_bp)
def create_app(config_map_list=None, blue_print_list=[]):
    app = Flask(__name__)
    for m in config_map_list:
        app.config.update(m)
        
    db.init_app(app)
    migrate.init_app(app, db)
    
    for bp in blue_print_list:
        app.register_blueprint(bp)
    
    return app