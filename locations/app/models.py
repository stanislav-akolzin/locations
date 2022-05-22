from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Region(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class City(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'), nullable=False)
    region = db.relationship('Region', backref=db.backref('cities', cascade='all,delete', lazy=True))

    def __init__(self, name, region):
        self.name = name
        self.region_id = region


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'{self.id}:{self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

