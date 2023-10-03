from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Breed(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True, nullable=False)

        # Define a relationship to the pets
        pets = db.relationship('Pet', backref='breed', lazy=True)

        def __repr__(self):
            return f'<Breed {self.name}>'


class FavoritePet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    favorite_date = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<FavoritePet {self.id}>'


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)

    # Define a relationship to the posted pets
    posted_pets = db.relationship('PostedPet', backref='administrator', lazy=True)

    def __repr__(self):
        return f'<Administrator {self.username}>'


class PostedPet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('administrator.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    posting_date = db.Column(db.TIMESTAMP, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('pet_status.id'), nullable=False)

    def __repr__(self):
        return f'<PostedPet {self.id}>'


class PetStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # Define a relationship to the posted pets
    posted_pets = db.relationship('PostedPet', backref='status', lazy=True)

    def __repr__(self):
        return f'<PetStatus {self.name}>'


class AdoptionApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    submission_date = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'<AdoptionApplication {self.id}>'


