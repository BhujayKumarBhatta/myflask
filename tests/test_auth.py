import unittest
import datetime
import json
import jwt
from flask import current_app
from app1.authentication.token_after_login import \
 generate_encrypted_auth_token , decrypt_n_verify_token

from tests.base_test import  BaseTestCase

#app.app_context().push()


class TestToken(BaseTestCase):
    '''
    (venvp3flask) bhujay@DESKTOP-DTA1VEB:/mnt/c/mydev/myflask$ python -m unittest discover tests
    '''
      
    def test_auth_token_with_actual_rsa_keys(self):
        
        user_from_db = {
            'id': '001',
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
        self.assertTrue(isinstance(auth_token, str))     
           
        
        np = decrypt_n_verify_token(auth_token, __publickey)
        self.assertTrue(isinstance(np, dict))
        self.assertEqual(np.get('sub'), payload.get('sub'))
          
    
  
    def test_route_for_token_generation(self):
        with self.client:
            response = self.client.post(
                '/token/gettoken',
                data=json.dumps(dict(
                    username='susan',
                    password='myserect' )),
                content_type='application/json')
            print('response is {}'.format(response))
            data = json.loads(response.data.decode())
            print(data['message'])
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)
        
        