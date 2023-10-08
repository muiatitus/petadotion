from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Define a one-to-many relationship with pets
    pets = relationship('Pet', backref='owner', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def update_profile(self, **kwargs):
        # Update user profile fields
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        # Save the changes to the database
        db.session.commit()


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    is_adopted = db.Column(db.Integer, default=0)  # 0 for available, 1 for adopted
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Define a foreign key relationship with users
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, type, breed, age, description, owner_id):
        self.name = name
        self.type = type
        self.breed = breed
        self.age = age
        self.description = description
        self.owner_id = owner_id
