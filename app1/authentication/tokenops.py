from flask import request, Blueprint, jsonify, current_app,make_response
import jwt
import datetime


token_bp = Blueprint('token_bp', __name__)

# don't try to access it here to avoid RuntimeError: Working outside of application context
#publickey = current_app.config.get('public_key') 

@token_bp.route('/token/GET')
def get_token():
    '''
     curl -X GET  localhost:5000/token/GET
     '''
    privkey = current_app.config.get('private_key')
    
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
        'iat': datetime.datetime.utcnow(),
        'sub': 'bhujay'
         }
    try:
        auth_token = jwt.encode(
            payload,
            privkey,
            algorithm='RS256'
        )
        responseObject = {
            'status': 'success',
            'message': '',
            'auth_token': auth_token.decode()}
#         return auth_token
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        return e
    
@token_bp.route('/token/verify', methods=['POST'])
def verify_token():    
    '''
    curl -X POST -d '{"auth_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDM4NDQ3NTAsInN1YiI6ImJodWpheSIsImlhdCI6MTU0Mzg0NDc0NX0.GjFWcz65I4ed0IGChU4zjjSpDV-2DXCryIrgNRLKZ0o"}'  -H "Content-Type: Application/json"  localhost:5000/token/verify
    '''
    publickey = current_app.config.get('public_key') 
    if request.method == 'POST':
        if 'auth_token' in request.json:
            auth_token = request.json['auth_token']
    try:
        payload = jwt.decode(
            auth_token,
            publickey,
            algorithm=['RS512']
        )
        
        print(payload.get('sub'))
#         subject_in_token = "decrypted token data is %s" % payload.get('subject')
#         name = subject_in_token.get('name')
#         
        return "Data in token is %s \nand subject in payload is %s \n" % (payload, payload.get('sub'))
    except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
#     except Exception as e:
#         return e   

# '''
# Following are the claim attributes :
# iss: The issuer of the token
# sub: The subject of the token
# aud: The audience of the token
# qsh: query string hash
# exp: Token expiration time defined in Unix time
# nbf: “Not before” time that identifies the time before which the JWT must not be accepted for processing
# iat: “Issued at” time, in Unix time, at which the token was issued
# jti: JWT ID claim provides a unique identifier for the JWT
# 
# '''
