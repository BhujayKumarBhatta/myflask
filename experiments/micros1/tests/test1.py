import unittest
# from flask import Flask
from flask_testing import TestCase
import json
import ms2app

from ms2app.APIroutes.firstapi import bp1

bp_list = [bp1]

app = ms2app.create_app(blue_print_list=bp_list)

class BaseTestCase(TestCase):
    def create_app(self):       
        return app       
  
    def test_first_api(self):
        with self.client:
            response = self.client.post('/simpleapi')
            print(response.data.decode())
            #return_data = json.loads(response)
            return_data = json.loads(response.data.decode())
            self.assertTrue(return_data['message'] == 'Catch me if you can')
            

if __name__ =='__main__':
    unittest.main()
    
