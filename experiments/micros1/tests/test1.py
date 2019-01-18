import unittest
# from flask import Flask
from flask_testing import TestCase
import json
import ms2app
from auth import authclient

from ms2app.APIroutes.firstapi import bp1

bp_list = [bp1]

app = ms2app.create_app(blue_print_list=bp_list)

class BaseTestCase(TestCase):
    def create_app(self):       
        return app     
    
    def test_get_token(self):
        response = authclient.get_token('susan', 'mysecret', 'http://localhost:5001' )
        self.assertTrue(isinstance(response, str))                              
#         data = json.loads(response.decode())
#         print(data)
#         self.assertTrue(data['status'] == 'success')
#         self.assertTrue('auth_token' in data)
#     
    def test_verify_token(self):
        token = authclient.get_token('susan', 'mysecret', 'http://localhost:5001' )
        result = authclient.verify_token(token, 'http://localhost:5001' )
        self.assertTrue(isinstance(result, dict))
        

        
  
    def test_first_api(self):
        with self.client:
            response = self.client.post('/simpleapi')
            print(response.data.decode())
            #return_data = json.loads(response)
            return_data = json.loads(response.data.decode())
            self.assertTrue(return_data['message'] == 'Catch me if you can')
            
    def test_ep2(self):
        response = authclient.get_token('susan', 'mysecret', 'http://localhost:5001' )
        self.assertTrue(isinstance(response, str))         
        with self.client:
            response = self.client.post('/ep2', data=json.dumps(dict(
                    auth_token=response,
                    )),
                content_type='application/json')
            print(response.data.decode())            
            #return_data = json.loads(response)
            return_data = json.loads(response.data.decode())
            self.assertTrue(return_data['message'] == 'Catch me if you can')
            print('ep2 tested ok')
                        

if __name__ =='__main__':
    unittest.main()
    
