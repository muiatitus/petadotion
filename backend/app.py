from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager, UserMixin  # Import LoginManager
from routes.auth import auth_bp
from routes.pets import pets_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Change to your database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.secret_key = 'your_secret_key'  # Replace with your secret key
app.config['SESSION_TYPE'] = 'filesystem'  # Choose a session storage method

# Initialize Flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)  # Enable CORS for all routes

login_manager = LoginManager()
login_manager.init_app(app)

from flask_jwt_extended import JWTManager  # Import JWTManager after creating the Flask app

jwt = JWTManager(app)  # Initialize JWTManager after creating the Flask app

@app.before_first_request
def create_tables():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    # Implement a function to load a user based on the user_id
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(pets_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
