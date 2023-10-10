import unittest
from yourapp import create_app, db
from yourapp.models import User

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config_test.py')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        # Test user registration
        response = self.app.test_client().post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)

    def test_login_user(self):
        # Test user login
        # First, create a user to login
        user = User(username='testuser', email='test@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        response = self.app.test_client().post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_logout_user(self):
        # Test user logout
        # First, create a user and log them in
        user = User(username='testuser', email='test@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        login_response = self.app.test_client().post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(login_response.status_code, 200)

        # Now, logout the user
        logout_response = self.app.test_client().get('/logout')
        self.assertEqual(logout_response.status_code, 200)
        self.assertIn(b'Logged out successfully', logout_response.data)

if __name__ == '__main__':
    unittest.main()
