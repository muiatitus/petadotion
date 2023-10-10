import unittest
from app import app, db
from models import User, Pet

class PetsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a test database
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_create_pet(self):
        # Register a test user and get the access token
        response = self.app.post('/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        data = response.get_json()
        access_token = data['access_token']

        # Create a new pet listing
        response = self.app.post('/pets', json={
            'name': 'Test Pet',
            'type': 'Dog',
            'breed': 'Golden Retriever',
            'age': 2,
            'description': 'A friendly dog'
        }, headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 201)

    def test_get_all_pets(self):
        # Retrieve all pets
        response = self.app.get('/pets')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
