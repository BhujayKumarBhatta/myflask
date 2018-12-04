from flask import request, Blueprint, jsonify
import jwt
import datetime

token_bp = Blueprint('token_bp', __name__)

__SECRET_kEY = 'Mysupersretkey'


@token_bp.route('/token/GET')
def get_token():
    '''
     curl -X GET  localhost:5000/token/GET
     '''
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
        'iat': datetime.datetime.utcnow(),
        'sub': 'bhujay' }
    try:
        auth_token = jwt.encode(
            payload,
            __SECRET_kEY,
            algorithm='HS256'
        )
        return auth_token
    except Exception as e:
        return e
    
@token_bp.route('/token/verify', methods=['POST'])
def verify_token():    
    '''
    curl -X POST -d '{"auth_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDM4NDQ3NTAsInN1YiI6ImJodWpheSIsImlhdCI6MTU0Mzg0NDc0NX0.GjFWcz65I4ed0IGChU4zjjSpDV-2DXCryIrgNRLKZ0o"}'  -H "Content-Type: Application/json"  localhost:5000/token/verify
    '''
    if request.method == 'POST':
        if 'auth_token' in request.json:
            auth_token = request.json['auth_token']
    try:
        payload = jwt.decode(
            auth_token,
            __SECRET_kEY,
            algorithm=['HS256']
        )
        data_in_token = "decrypted token data is %s" % payload
        return data_in_token
    except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
#     except Exception as e:
#         return e   

'''
Following are the claim attributes :
iss: The issuer of the token
sub: The subject of the token
aud: The audience of the token
qsh: query string hash
exp: Token expiration time defined in Unix time
nbf: “Not before” time that identifies the time before which the JWT must not be accepted for processing
iat: “Issued at” time, in Unix time, at which the token was issued
jti: JWT ID claim provides a unique identifier for the JWT

'''
