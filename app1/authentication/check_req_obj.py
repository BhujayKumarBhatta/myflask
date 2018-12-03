from flask import Blueprint, request, make_response, jsonify
from flask.globals import session
import json
#from flask.views import MethodView

req_obj_bp = Blueprint('check_req_obj', __name__)

@req_obj_bp.route('/check-req-obj', methods=['GET', 'POST'])
def check_req_obj():
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
    
    
        'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_route',
    'application', 'args', 'authorization', 'base_url', 'blueprint', 'cache_control',
    'charset', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type',
    'cookies', 'data', 'date', 'dict_storage_class', 'disable_data_descriptor',
    'encoding_errors', 'endpoint', 'environ', 'files',
    'form', 'form_data_parser_class', 'from_values', 'full_path',
    'get_data', 'get_json', 'headers', 'host', 'host_url',
    'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since',
    'input_stream', 'is_json', 'is_multiprocess', 'is_multithread',
    'is_run_once', 'is_secure', 'is_xhr', 'json', 'list_storage_class',
    'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_forwards',
    'method', 'mimetype', 'mimetype_params', 'module', 'on_json_loading_failed',
    'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer',
    'remote_addr', 'remote_user', 'routing_exception', 'scheme', 'script_root',
    'shallow', 'stream', 'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule',
    'user_agent', 'values', 'view_args', 'want_form_data_parsed']"   
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
                                 "request.authorization = %s \n"
                                 "request.endpoint = %s \n"
                                 "request.application = %s \n"
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
                                    request.authorization,
                                    request.endpoint,
                                    request.application,
                                    session
                                    )
                                 )
                               
       
        return inside_request_object
#     return request.method





