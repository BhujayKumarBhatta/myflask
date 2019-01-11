from flask import Blueprint,  jsonify

bp1 = Blueprint('bp1', __name__)

@bp1.route('/simpleapi', methods=['GET', 'POST'])
def simpleapi():
    resp = {'message': 'Catch me if you can'}
    return jsonify(resp)
