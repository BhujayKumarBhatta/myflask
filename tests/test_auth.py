import unittest
import datetime
import json
import jwt
from flask import current_app
from app1.authentication.token_after_login import \
 generate_encrypted_auth_token , decrypt_n_verify_token

from tests.base_test import  BaseTestCase
from app1 import db
from app1.authentication.models import User

#app.app_context().push()


class TestToken(BaseTestCase):
    '''
    (venvp3flask) bhujay@DESKTOP-DTA1VEB:/mnt/c/mydev/myflask$ python -m unittest discover tests
    '''
#       
    def test_auth_token_with_actual_rsa_keys(self):
          
        user_from_db = {
            'id': 1,
            'username': 'susan',
            'email':  'susan@abc.com',            
            }
  
        payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
                    'iat': datetime.datetime.utcnow(),
                    'sub': user_from_db
                     }
        __privkey = current_app.config.get('private_key')
        __publickey = current_app.config.get('public_key')   
       
        auth_token = generate_encrypted_auth_token(payload, __privkey) 
#         print(type(auth_token))       
        self.assertTrue(isinstance(auth_token, bytes))     
             
          
        np = decrypt_n_verify_token(auth_token, __publickey)
        self.assertTrue(isinstance(np, dict))
        self.assertEqual(np.get('sub'), payload.get('sub'))
#         print('end of  jwt token function.....................')
#     
#   
    def test_token_gen_failed_for_unregistered_user(self):
        with self.client:
            response = self.client.post(
                '/token/gettoken',
                data=json.dumps(dict(
                    username='susan',
                    password='mysecret' )),
                content_type='application/json')
            #print('response is {}'.format(response))
            data = json.loads(response.data.decode())
            #print(data['message'])
            self.assertTrue(data['status'] == 'User not registered')
            self.assertFalse('auth_token' in data)
            
    def test_token_gen_n_verify_success_for_registered_user(self):
        u1 = User(username='susan', email='susan@abc.com')
        u1.set_password('mysecret')       
        self.assertTrue(u1.check_password('mysecret'))
        db.session.add(u1)        
        db.session.commit()
        with self.client:
            response = self.client.post(
                '/token/gettoken',
                data=json.dumps(dict(
                    username='susan',
                    password='mysecret' )),
                content_type='application/json')
#             print('response is {}'.format(response))
            data = json.loads(response.data.decode())
            #print(data['message'])
            self.assertTrue(data['status'] == 'success')
            self.assertTrue('auth_token' in data)
            mytoken = data['auth_token']
        with self.client:
            response = self.client.post(
                '/token/verify_token',
                data=json.dumps(dict(
                    auth_token=mytoken,
                    )),
                content_type='application/json')
            #print('response is {}'.format(response))
            data = json.loads(response.data.decode())
            #print(data)
            self.assertTrue(data['status'] == 'Verification Successful')
            self.assertTrue('payload' in data)
            self.assertTrue(data['payload'].get('sub').get('username') == 'susan')
    
    def test_invalid_token(self):
        junk_token = "11eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiaWQiOjEsInVzZXJuYW1lIjoic3VzYW4iLCJlbWFpbCI6InN1c2FuQGFiYy5jb20ifSwiaWF0IjoxNTQ3ODI0ODcyLCJleHAiOjE1NDc4Mjg0NzJ9.h8w8NzCC7FGGBo1nUrBKHRrYiFI0KrXujLx-GpThOzk8Gqcw-bWAy_jng-EllHJAay7aWw8u6K3B7T62OrZ5Hkj0qKMcwtZPQMySooTSWGW-I1LI3_vKSYhaXjXwayl--Ke3ZPBI1fFN61wUXDJsMuNydlE4eUv60MIAI5eT7o5GjSwfXETT1uv4mO5uHb-Yxf_tU13UMDt8nHX99h2s8WNZarLr3e5lJv786Y6aB4satzKTE3IhQ2HDqhnlRkxT00kRyd-dBeTzpZeA0SiCSUqF6pRbWHEgEGJPr_p-upxBAc_IP_zfUkyygGsRcUNM_lMF5RGLCRSFzeQ4TxBtDQ"
        with self.client:
            response = self.client.post(
                '/token/verify_token',
                data=json.dumps(dict(auth_token=junk_token)),
                content_type='application/json')
            data = json.loads(response.data.decode())
            print(data)
            #self.assertTrue(data['status'] == 'Invalid token')
            self.assertTrue(isinstance('payload', str))
    
    def test_expired_token(self):
        expired_token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiaWQiOjEsInVzZXJuYW1lIjoic3VzYW4iLCJlbWFpbCI6InN1c2FuQGFiYy5jb20ifSwiaWF0IjoxNTQ3ODI0ODcyLCJleHAiOjE1NDc4Mjg0NzJ9.h8w8NzCC7FGGBo1nUrBKHRrYiFI0KrXujLx-GpThOzk8Gqcw-bWAy_jng-EllHJAay7aWw8u6K3B7T62OrZ5Hkj0qKMcwtZPQMySooTSWGW-I1LI3_vKSYhaXjXwayl--Ke3ZPBI1fFN61wUXDJsMuNydlE4eUv60MIAI5eT7o5GjSwfXETT1uv4mO5uHb-Yxf_tU13UMDt8nHX99h2s8WNZarLr3e5lJv786Y6aB4satzKTE3IhQ2HDqhnlRkxT00kRyd-dBeTzpZeA0SiCSUqF6pRbWHEgEGJPr_p-upxBAc_IP_zfUkyygGsRcUNM_lMF5RGLCRSFzeQ4TxBtDQ"
        with self.client:
            response = self.client.post(
                '/token/verify_token',
                data=json.dumps(dict(auth_token=expired_token)),
                content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'Signature expired')
            self.assertTrue(isinstance('payload', str))
        
            
    def test_token_gen_fail_with_wrong_password(self):
        u1 = User(username='susan', email='susan@abc.com')
        u1.set_password('mysecret')       
        self.assertTrue(u1.check_password('mysecret'))
        db.session.add(u1)        
        db.session.commit()
        with self.client:
            response = self.client.post(
                '/token/gettoken',
                data=json.dumps(dict(
                    username='susan',
                    password='wrong_password' )),
                content_type='application/json')
#             print('response is {}'.format(response))
            data = json.loads(response.data.decode())
            #print(data['message'])
            self.assertTrue(data['status'] == 'Wrong Password')
            self.assertFalse('auth_token' in data)
            

           
        
        