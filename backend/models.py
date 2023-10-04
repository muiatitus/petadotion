from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    breed = db.relationship('Breed', backref=db.backref('pets'))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    adoption_status = db.Column(db.String(20))
    price = db.Column(db.Float)

class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100), nullable=False)

class FavoritePet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('favorite_pets'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    pet = db.relationship('Pet', backref=db.backref('favorited_by'))
    favorite_date = db.Column(db.DateTime, nullable=False)

class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

class PostedPet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('administrator.id'), nullable=False)
    admin = db.relationship('Administrator', backref=db.backref('posted_pets'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    pet = db.relationship('Pet', backref=db.backref('posted_by'))
    posting_date = db.Column(db.DateTime, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('pet_status.id'), nullable=False)
    status = db.relationship('PetStatus', backref=db.backref('posted_pets'))

class PetStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(50), nullable=False)

class AdoptionApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('adoption_applications'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    pet = db.relationship('Pet', backref=db.backref('applications'))
    status = db.Column(db.String(20))
    submission_date = db.Column(db.DateTime, nullable=False)