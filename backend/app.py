from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'skrky'  # Set the secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Import your routes and register them with the app
from routes import auth_routes, pet_routes, favorite_routes, application_routes
app.register_blueprint(auth_routes)
app.register_blueprint(pet_routes)
app.register_blueprint(favorite_routes)
app.register_blueprint(application_routes)

@app.route('/', methods=['GET'])
def index():
    return jsonify(message='Server is running')

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')  # Update with your frontend URL
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

if __name__ == '__main__':
    app.run()