from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'skrky'  # Set the secret key
db = SQLAlchemy(app)

# Import your routes and register them with the app
from routes import auth_routes, pet_routes, favorite_routes, application_routes
app.register_blueprint(auth_routes)
app.register_blueprint(pet_routes)
app.register_blueprint(favorite_routes)
app.register_blueprint(application_routes)
if __name__ == '__main__':
    app.run()
