from flask import url_for
from flask_testing import TestCase
from application import app, pilot_name

# from application import app
# from application import pilot_name

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_pilot(self):

        for i in range(10):
            response = self.client.get(url_for('get_pilot'))

            self.assert200(response)
            self.assertIn(response.data.decode(), pilot_name)