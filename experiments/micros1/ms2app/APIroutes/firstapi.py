from flask import Blueprint,  jsonify
from auth import  authclient

bp1 = Blueprint('bp1', __name__)

@bp1.route('/simpleapi', methods=['GET', 'POST'])
@authclient.deco2
def simpleapi():
    resp = {'message': 'Catch me if you can'}
    return jsonify(resp)


@bp1.route('/ep2', methods=['GET', 'POST'])
@authclient.validate_request
def ep2():
    resp = {'message': 'Catch me if you can'}
    return jsonify(resp)

