from flask_testing import TestCase
from flask import url_for, Response
import requests_mock
import pytest
from unittest.mock import patch

from front_end_api.application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index_get(self):       
            
        pilot = "Sullustan"
        tier = "A Tier"
        json ={
            "pilot": "Sullustan",
            "tier": "A Tier",
            "message": "amassing near Sullust"
        } 

        with requests_mock.Mocker() as m:
            m.get('http://pilot_api:5000/get_pilot', text=pilot)
            m.get('http://tier_api:5000/get_tier', text=tier)
            m.post('http://service_4:5000/post/status', json=json)

            response = self.client.get(url_for('index'))


        self.assertEqual(response.status_code, 200)
        self.assertIn("Sullustan", response.data.decode())
        self.assertIn("A Tier", response.data.decode())
        self.assertIn("Amassing near Sullust", response.data.decode())

        # with patch ("random.choice") as g:
        #     g.return_value.text = "Interceptor"

        #     response = self.client.get(url_for('index'))
        #     assert response.status_code == 200
        #      self.assertIn(b'Interceptor', response.data)
            
