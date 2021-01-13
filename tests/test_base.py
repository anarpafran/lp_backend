from flask_testing import TestCase
from main import app
from flask import current_app, url_for, json

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


    def test_app_exists(self):
        self.assertIsNotNone(current_app)


    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])


    def test_applications_code200(self):
        data = {'tax_id':'1234567890', 'business_name': 'LF', 'requested_amount': '1'}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url_for('applications'), data=json.dumps(data), headers=headers)
        self.assert200(response)


    def test_applications_declined(self):
        data = {'tax_id':'1234567890', 'business_name': 'LF', 'requested_amount': '70000'}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url_for('applications'), data=json.dumps(data), headers=headers)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['state'], 'Declined')


    def test_applications_undecided(self):
        data = {'tax_id':'1234567890', 'business_name': 'LF', 'requested_amount': '50000'}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url_for('applications'), data=json.dumps(data), headers=headers)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['state'], 'Undecided')


    def test_applications_approved(self):
        data = {'tax_id':'1234567890', 'business_name': 'LF', 'requested_amount': '20000'}
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url_for('applications'), data=json.dumps(data), headers=headers)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['state'], 'Approved')