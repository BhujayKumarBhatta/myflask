from flask import Blueprint, request, make_response, jsonify
from flask.globals import session
import json
#from flask.views import MethodView

token_bp = Blueprint('tokenops', __name__)

@token_bp.route('/check-req-obj', methods=['GET', 'POST'])
def get_token():
    '''
    check request object  
    curl -X POST --header "Content-Type: application/json"  -d '{"username": "bhujay"}' localhost:5000/token
    
    bhujay@DESKTOP-DTA1VEB:/mnt/c/Windows/System32$ curl -X POST   -d '{"username": "bhujay"}' localhost:5000/token
    request.json = None
    request.data = b''
    request.form = ImmutableMultiDict([('{"username": "bhujay"}', '')])
    jsonify(request.form) = <Response 34 bytes [200 OK]>
    request.get_data() = b''
    
    #observe that when the content-type  header is not json form has the data otherwise request.data has the data
    
    bhujay@DESKTOP-DTA1VEB:/mnt/c/Windows/System32$ curl -X POST --header "Content-Type: application/json"  -d '{"username": "bhujay"}' localhost:5000/token
    request.json = {'username': 'bhujay'}
    request.data = b'{"username": "bhujay"}'
    request.form = ImmutableMultiDict([])
    jsonify(request.form) = <Response 3 bytes [200 OK]>
    request.get_data() = b'{"username": "bhujay"}'   
    '''
    if  request.method == 'POST' or request.method == 'GET':
        inside_request_object = ("request.json = %s \n" 
                                 "request.data = %s \n" 
                                 "request.form = %s \n" 
                                 "jsonify(request.form) = %s \n"
                                 "request.get_data() irrespective of content-type = %s \n"
                                 "request.values = %s \n"
                                 "jsonify(request.values) = %s \n"
                                 "request.headers = %s \n" 
                                 "request.environ = %s \n"
                                 "session = %s \n"
                                 
                                 % (request.json,
                                    request.data,
                                    request.form,
                                    jsonify(request.form),
                                    request.get_data(),
                                    request.values,
                                    jsonify(request.values),
                                    request.headers,
                                    request.environ,
                                    session
                                    )
                                 )
                               
       
        return inside_request_object
#     return request.method





