# import app1
# # from app1 import flask_app_var
# 
# app = app1.create_app()

#@flask_app_var.route('/')
@app.route('/')
def hello():
    return 'Hello World'   