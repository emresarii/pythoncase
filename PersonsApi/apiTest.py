import unittest
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:5000/persons'
        
    def test_get_request(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))
        self.assertTrue(len(response.json()) > 0)
        self.assertTrue(all(isinstance(p, dict) for p in response.json()))
        self.assertTrue(all('id' in p and 'firstName' in p and 'lastName' in p and 'email' in p  and 'createdDate' in p for p in response.json()))