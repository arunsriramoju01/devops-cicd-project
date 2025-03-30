import app
import unittest

class TestApp(unittest.TestCase):
    def test_hello(self):
        client = app.app.test_client()
        response = client.get('/')
        assert response.status_code == 200
