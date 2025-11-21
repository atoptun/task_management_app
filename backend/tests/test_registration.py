import unittest
from flask_testing import TestCase
from app import app, db
from app.models.models import User


class TestRegistrationAPI(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_successful_registration(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'User registered successfully'})

    def test_registration_without_username(self):
        response = self.client.post('/register', json={
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Username and password required'})

    def test_duplicate_registration(self):
        # First registration should succeed
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Duplicate registration should fail
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json, {'message': 'User already exists'})


if __name__ == '__main__':
    unittest.main()