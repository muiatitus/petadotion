import unittest
from app import app, db  # Import your Flask app and database object
from models import User, Pet  # Import User and Pet models
import json

class PetsTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

        # Create a test database and tables
        db.create_all()

        # Create a test user
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Create a test pet
        pet = Pet(name='Test Pet', type='Dog', breed='Labrador', age=2, description='A friendly dog', owner_id=user.id)
        db.session.add(pet)
        db.session.commit()

        # Log in as the test user and get an access token
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        login_response = self.app.post('/login', data=json.dumps(login_data), content_type='application/json')
        login_data = json.loads(login_response.data.decode())
        self.access_token = login_data['access_token']

    def tearDown(self):
        # Drop the test database and tables
        db.session.remove()
        db.drop_all()

    def test_get_all_pets(self):
        # Test getting a list of all available pets
        response = self.app.get('/pets', headers={'Authorization': f'Bearer {self.access_token}'})
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    def test_get_pet_details(self):
        # Test getting details of a specific pet
        response = self.app.get('/pets/1', headers={'Authorization': f'Bearer {self.access_token}'})
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Test Pet')

    def test_create_pet_listing(self):
        # Test creating a new pet listing
        data = {
            'name': 'New Pet',
            'type': 'Cat',
            'breed': 'Siamese',
            'age': 3,
            'description': 'A lovely cat'
        }
        response = self.app.post('/pets', data=json.dumps(data), content_type='application/json', headers={'Authorization': f'Bearer {self.access_token}'})
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Pet listing created successfully')

    # Add more test cases for other pet-related routes as needed

if __name__ == '__main__':
    unittest.main()
