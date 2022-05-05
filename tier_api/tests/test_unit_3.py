from flask import url_for, Response
from flask_testing import TestCase

from tier_api.app import app, tier_choice


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_tier(self):

        for i in range(10):
            response = self.client.get(url_for('name'))
            self.assert200(response)
            self.assertIn(response.data.decode(), tier_choice)