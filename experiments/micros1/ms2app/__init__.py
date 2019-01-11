from flask import Flask

def create_app(config_map_list=None, blue_print_list=None):
    app = Flask(__name__)
    if config_map_list:
        for m in config_map_list:
            app.config.update(m)     
   
    
    if blue_print_list:
        for bp in blue_print_list:
            app.register_blueprint(bp)
    
    return app