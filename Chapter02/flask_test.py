import os, sys

# Inject where we are into syspath to avoid setting PYTHONPATH.
whereWeAre = os.path.dirname(os.path.realpath(__file__))
position = whereWeAre.rfind('/')
print (whereWeAre)
print (whereWeAre[:position]+ '\n')
sys.path.insert(1, whereWeAre[:position + 1])

from app import app
import unittest

class FlaskappTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_users_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/users')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_tweets_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v2/tweets')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_info_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/info')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_add_users_status_code(self):
        # sends HTTP POST request to the application
        result = self.app.post('/api/v1/users', data='{"username":"salim47", "email":"salim47@gmail.com", "password": "test123"}',
                               content_type='application/json')
        print (result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 409)


    def test_update_users_status_code(self):
        # sends HTTP POST request to the application
        result = self.app.put('/api/v1/users/32', data='{"password": "testing12345", "full_name":"Salimmmmm"}',
                               content_type='application/json')
        print (result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


    def test_delete_users_status_code(self):
        # sends HTTP DELETE request to the application
        result = self.app.delete('/api/v1/users', data='{"username":"salim20"}',
                               content_type='application/json')
        print (result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 404)


    def test_add_tweets_status_code(self):
        # sends HTTP POST request to the application
        result = self.app.post('/api/v2/tweets', data='{"username":"salim11", "body": "Wow Now! is it really working"}',
                               content_type='application/json')
        print (result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 201)