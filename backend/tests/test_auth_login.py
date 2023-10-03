import unittest
from app import app, db
from models import User
import json


class AuthLoginTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a separate test database
        self.app = app.test_client()
        db.create_all()

        # Create a test user for authentication
        user = User(username='testuser', email='test@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_successful(self):
        response = self.app.post('/auth/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_login_failed(self):
        response = self.app.post('/auth/login', json={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid credentials', response.data)

if __name__ == '__main__':
    unittest.main()
