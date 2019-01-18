import flask
from flask import request
import requests
import json
import functools

auth_url = 'http://localhost:5001'

def get_token(username, password, auth_endpoint):
#     print('get token function initaited')   
#     data=json.dumps(dict(username='susan', password='mysecret'))
    data=json.dumps(dict(username=username, password=password))
    url= auth_endpoint+'/token/gettoken'
    headers={'content-type':'application/json'}
    r = requests.post(url, data, headers=headers)
    #print(r.content)
#     return r.content
    r_dict = json.loads(r.content.decode())                  
    if r_dict['status'] == 'success': 
        token_received = r_dict['auth_token'] 
#         print('got the token as : {}'.format(token_received))   
    return token_received

def verify_token(token, auth_endpoint):
    print('sending token for verifiaction')  
    url = auth_endpoint+'/token/verify_token'
    headers={'content-type':'application/json'}
    data=json.dumps(dict(
                    auth_token=token,
                    ))
    r = requests.post(url, data, headers=headers)   
#     print(r.content)
#     print(type(r.content))
    r_dict = json.loads(r.content.decode())  
    return r_dict
    if r_dict['status'] == 'Verification Successful' :
        if 'payload' in r_dict:
            username = r_dict['payload'].get('sub').get('username') 
            role = r_dict['payload'].get('sub').get('role')
            result = {'username': username, 'role': role}
        #print(result)
        return result
    



def deco2(f):
    auth_url = 'http://localhost:5001'
    token = get_token('susan', 'mysecret', auth_url)
    '''
    getting token at this stage  shoukd be some other functions responsibility
    '''
    token_verification_result = verify_token(token, auth_url)
    '''
    if toekn expired get fresh toekn
    '''
    if token_verification_result['status'] == 'Verification Successful' :
        username = token_verification_result['payload'].get('sub').get('username') 
        role = token_verification_result['payload'].get('sub').get('role')
        if role != 'abc':
            return f

def validate_request(f):
  @functools.wraps(f)
  def decorated_function(*args, **kws):
    # Do something with your request here
    fdata = flask.request.get_json()
    if not fdata:
      flask.abort(404)
    if 'auth_token' in fdata:
            auth_token = fdata['auth_token']
            token_verification_result = verify_token(auth_token, auth_url)
            print(token_verification_result)
            if token_verification_result['status'] == 'Verification Successful' :
#                 print(token_verification_result)
#                 print(type(token_verification_result))               
                username = token_verification_result['payload'].get('sub').get('username') 
                role = token_verification_result['payload'].get('sub').get('role')
                if role != 'abc':
                    #do more stuff
                    return f(*args, **kws)
                #handle else for authentication errors
            #handle {'message': 'Token has been successfully decrypted', 'payload': 'Signature expired. Please log in again.', 'status': 'Verification Successful'}
  return decorated_function

  
def deco3(f):      
    if request.method == 'POST':
        if 'auth_token' in request.json:
            auth_token = request.json['auth_token']
        
    token_verification_result = verify_token(auth_token, auth_url)
    '''
    if toekn expired get fresh toekn
    '''
    if token_verification_result['status'] == 'Verification Successful' :
        username = token_verification_result['payload'].get('sub').get('username') 
        role = token_verification_result['payload'].get('sub').get('role')
        if role != 'abc':
            return f
           

    
               
def deco1(f):
    def wrapper_func(*args, **kwargs):
            print('invoking call to get token')
            data=json.dumps(dict(username='susan', password='mysecret'))
            url= 'http://localhost:5001/token/gettoken'
            headers={'content-type':'application/json'}
            r = requests.post(url, data, headers=headers)
            print(r.content)    
            print(type(r.content))  
            r_dict = json.loads(r.content.decode())                  
            if r_dict['status'] == 'success': 
                token_received = rdict['auth_token']
                result = f(*args, **kwargs) 
            else:
                pass # we have to handle how to show the failure result here 
            return result
    return wrapper_func
        
  
def token_auth_deco(username='susan', password='mysecret', auth_endpoint='http://localhost:5001'):
    def deco(original_function):
        def wrapper_func(*args, **kwargs):
            print('invoking call to get token')
            data=json.dumps(dict(username=username, password=password))
            url= auth_endpoint+'/token/gettoken'
            headers={'content-type':'application/json'}
            r = requests.post(url, data, headers=headers)
            print(r.content)                 
            result = original_function(*args, **kwargs)        
            return result
        return wrapper_func
    return deco



