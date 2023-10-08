import unittest
from ..app import app, db  # Import your Flask app and database object
from models import User  # Import the User model
import json

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

        # Create a test database and tables
        db.create_all()

    def tearDown(self):
        # Drop the test database and tables
        db.session.remove()
        db.drop_all()

    def test_register(self):
        # Test user registration
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.app.post('/register', data=json.dumps(data), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'User registered successfully')

    def test_register_existing_user(self):
        # Test user registration with an existing username
        user = User(username='existinguser', email='existinguser@example.com', password='existingpassword')
        db.session.add(user)
        db.session.commit()

        data = {
            'username': 'existinguser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.app.post('/register', data=json.dumps(data), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Username already exists')

    def test_login(self):
        # Test user login
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', data)

    def test_login_invalid_credentials(self):
        # Test user login with invalid credentials
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        data = {
            'username': 'testuser',
            'password': 'invalidpassword'
        }
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Invalid username or password')

if __name__ == '__main__':
    unittest.main()
