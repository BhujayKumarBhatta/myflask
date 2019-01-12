from flask import Blueprint,  jsonify
from auth import  authclient

bp1 = Blueprint('bp1', __name__)

@bp1.route('/simpleapi', methods=['GET', 'POST'])
@authclient.deco2
def simpleapi():
    resp = {'message': 'Catch me if you can'}
    return jsonify(resp)
