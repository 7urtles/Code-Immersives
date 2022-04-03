from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'

db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return f"{self.name} {self.species} {self.color}"

db.create_all()

def add_animals(some_animal):
    # creating Account class instances
    # use add_all() to add the list of Accounts
    db.session.add(some_animal)
    # commit changes to database
    db.session.commit()
    return True

def get_some_json():
	response = requests.get('http://136.34.32.221:5007/get_animals').json()
	return response

get_response = get_some_json()
for animal in get_response['animals']:
    new_animal = Animal(**get_response['animals'][animal])
    add_animals(new_animal)