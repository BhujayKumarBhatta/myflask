from app1.views import views_bp
@views_bp.route('/world')
def hello():
    return 'Hello World'   

