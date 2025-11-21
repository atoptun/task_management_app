import unittest
from app import app, db
from app.models.models import User, Task


class TestBasic(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()
        # with app.app_context():
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_registration(self):
        response = self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_task_creation(self):
        self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        access_token = self.app.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        }).json['access_token']

        response = self.app.post('/tasks', json={
            'title': 'Тестове завдання',
            'description': 'Тестовий опис',
            'owner_id': 1,
            'status': 'невиконано'
        }, headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
