# '''
# >>> dir(flask)
# ['Blueprint', 'Config', 'Flask', 'Markup', 'Request', 'Response', 'Session', 
# '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#  '__package__', '__path__', '__spec__', '__version__', '_app_ctx_stack', '_compat',
#   '_request_ctx_stack', 
# 'abort', 'after_this_request', 'app', 'appcontext_popped', 'appcontext_pushed', 
# 'appcontext_tearing_down', 'before_render_template', 'blueprints', 'cli', 'config',
# 'copy_current_request_context', 'ctx', 'current_app', 'escape', 'flash', 'g',
# 'get_flashed_messages', 'get_template_attribute', 'globals', 'got_request_exception',
# 'has_app_context', 'has_request_context', 'helpers', 'json', 'json_available', 'jsonify',
# 'logging', 'make_response', 'message_flashed', 'redirect', 'render_template', 
# 'render_template_string', 'request', 'request_finished', 'request_started', 
# 'request_tearing_down', 'safe_join', 'send_file', 'send_from_directory', 'session', 
# 'sessions', 'signals', 'signals_available', 'stream_with_context', 'template_rendered', 
# 'templating', 'url_for', 'wrappers']
# '''



from flask import Blueprint, request, make_response, jsonify
from flask.globals import session
import json
#from flask.views import MethodView

req_obj_bp = Blueprint('check_req_obj', __name__)

@req_obj_bp.route('/check-req-obj', methods=['GET', 'POST'])
def check_req_obj():
  
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
#     The return value from a view function is automatically converted into a response object for you 
# can return only string , tuple but can not multidictionary

'''
  '''
#     check request object  
#     curl -X POST --header "Content-Type: application/json"  -d '{"username": "bhujay"}' localhost:5000/token
#     
#     bhujay@DESKTOP-DTA1VEB:/mnt/c/Windows/System32$ curl -X POST   -d '{"username": "bhujay"}' localhost:5000/token
#     request.json = None
#     request.data = b''
#     request.form = ImmutableMultiDict([('{"username": "bhujay"}', '')])
#     jsonify(request.form) = <Response 34 bytes [200 OK]>
#     request.get_data() = b''
#     
#     #observe that when the content-type  header is not json form has the data otherwise request.data has the data
#     
#     bhujay@DESKTOP-DTA1VEB:/mnt/c/Windows/System32$ curl -X POST --header "Content-Type: application/json"  -d '{"username": "bhujay"}' localhost:5000/token
#     request.json = {'username': 'bhujay'}
#     request.data = b'{"username": "bhujay"}'
#     request.form = ImmutableMultiDict([])
#     jsonify(request.form) = <Response 3 bytes [200 OK]>
#     request.get_data() = b'{"username": "bhujay"}'
#     
#     
#         'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_route',
#     'application', 'args', 'authorization', 'base_url', 'blueprint', 'cache_control',
#     'charset', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type',
#     'cookies', 'data', 'date', 'dict_storage_class', 'disable_data_descriptor',
#     'encoding_errors', 'endpoint', 'environ', 'files',
#     'form', 'form_data_parser_class', 'from_values', 'full_path',
#     'get_data', 'get_json', 'headers', 'host', 'host_url',
#     'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since',
#     'input_stream', 'is_json', 'is_multiprocess', 'is_multithread',
#     'is_run_once', 'is_secure', 'is_xhr', 'json', 'list_storage_class',
#     'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_forwards',
#     'method', 'mimetype', 'mimetype_params', 'module', 'on_json_loading_failed',
#     'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer',
#     'remote_addr', 'remote_user', 'routing_exception', 'scheme', 'script_root',
#     'shallow', 'stream', 'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule',
#     'user_agent', 'values', 'view_args', 'want_form_data_parsed']"   
#     '''
# 
# 
# https://junxiandoc.readthedocs.io/en/latest/docs/flask/flask_cookie_session.html
# 
# Response to Request:
# Plain text string
# response object
# redirect(‘<ohter-url>’)
# abort(<error_code>)
# 
# 
# Get the args in the URL
# To access parameters submitted in the URL (?key=value):
# searchword = request.args.get('key', '')
# 
# 
# 5.3. Callback Functions
# Decorator to define callback function:
# 
# #@app.before_first_request # Only before the first request
# #@app.before_request # Before each request
# #@app.after_request # After each request if no exception
# #@app.teardown_request # After each request even there is exceptions
# 
# Global variable ‘g’ is valid in above functions. For example, we can use g.user to share login information among these functions.
# 
# 
# 6. Flask Response Object
# The return value from a view function is automatically converted into a response object for you. 
# If the return value is a string it’s converted into a response object with the string as response body,
#  an 200 OK error code and a text/html mimetype.
# The logic that Flask applies to converting return values into response objects is as follows:
# 
# 
# If a response object of the correct type is returned it’s directly returned from the view.
# 
# If it’s a string, a response object is created with that data and the default parameters.
# 
# If a tuple is returned the items in the tuple can provide extra information. 
# Such tuples have to be in the form (response, status, headers) where at least one item has
# to be in the tuple. The status value will override the status code and headers can be a list
# or dictionary of additional header values.
# 
# If none of that works, Flask will assume the return value is a valid WSGI application and convert
# that into a response object.
# 
# 
# If you want to get hold of the resulting response object inside the view, you can use the make_response() function. Imagine you have a view like this:
# #@app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404
# You just need to wrap the return expression with make_response() and get the response object to modify it, then return it:
# #@app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp
#     
#     
# '''








