from flask import url_for, Response
from flask_testing import TestCase
from requests_mock import mock

from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://pilot_api:5000/get_pilot', text='Bomber')
            m.get('http://tier_api:5000/get_tier', text="A Tier")
            m.post('http://service-4:5000/post/status', json={
                "pilot": "Bomber",
                "tier": "A Tier",
                "message": "What a bot!"
            })

            response = self.client.get(url_for('index'))


        self.assert200(response)
        self.assertIn("Bomber", response.data.decode())
        self.assertIn("A Tier", response.data.decode())
        self.assertIn("What a bot!", response.data.decode())