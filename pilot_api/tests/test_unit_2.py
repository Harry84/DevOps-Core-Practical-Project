from flask import url_for, Response
from flask_testing import TestCase

from pilot_api.app import app, pilot_choice


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_pilot(self):

        for i in range(10):
            response = self.client.get(url_for('name'))
            self.assert200(response)
            self.assertIn(response.data.decode(), pilot_choice)