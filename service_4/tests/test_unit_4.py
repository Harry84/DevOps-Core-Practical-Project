from flask import url_for, Response
from flask_testing import TestCase
from pilot_api.app import pilot_choice
from tier_api.app import tier_choice
from service_4.app import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):

    def test_get_message(self):

        # for i in pilot_choice:
        #     for j in tier_choice:

        #         json = {'pilot':i, 'tier':j}
            
        #         response = self.client.get(url_for('post_status'), json=json)

        #         self.assert200(response)

        #         if j == "S Tier":
        #             self.assertIn("God", response.data.decode())
        #         elif j == "A Tier":
        #             self.assertIn("Parent", response.data.decode())
        #         elif j == "B Tier":
        #             self.assertIn("day job", response.data.decode())
        #         else:
        #             self.assertIn("bot", response.data.decode())
    
        response = self.client.post(url_for('post_status'), json={"pilot": "Sullustan", "tier": "A Tier"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Parent', response.data)