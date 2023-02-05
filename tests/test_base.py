from flask_testing import TestCase
from main import app
from flask import current_app, url_for

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_testing_env(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        fake_data = {
            'username': 'fake_user',
            'pwd': 'fake_pwd'
        }
        response = self.client.post(url_for('hello'), data=fake_data)
        self.assertRedirects(response, url_for('index'))