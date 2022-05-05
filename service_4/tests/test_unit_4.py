from flask import url_for, Response
from flask_testing import TestCase
from pilot_api.app import pilot_choice
from service_4.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_tier(self):

        for i in pilot_choice:
            for j in range(50):

                json = {'pilot':i, 'tier':j}
            
                response = self.client.get(url_for('post_status'), json=json)

                self.assert200(response)

                if j == "S Tier":
                    self.assertIn("God", response.data.decode())
                elif j == "A Tier":
                    self.assertIn("Parent", response.data.decode())
                elif j == "B Tier":
                    self.assertIn("day job", response.data.decode())
                else:
                    self.assertIn("bot", response.data.decode())