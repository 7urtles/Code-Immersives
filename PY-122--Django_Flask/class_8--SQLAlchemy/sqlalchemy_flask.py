from flask import Flask
# using the flask install of SQLAlchemy for ease of use integrating sqlalchemy later
from flask_sqlalchemy import SQLAlchemy
# will be used to view database tables and information
from sqlalchemy import inspect

app = Flask(__name__)
# Disabling a soon to be depricated option to kill the warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# setting the database type and name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# a class to act as a model for adding users to the table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # re-define what is shown when you print the class instance
    def __repr__(self):
        return '<User %r>' % self.username

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(80), unique=True, nullable=False)
    animal_type = db.Column(db.String(80), unique=False, nullable=False)
    animal_breed = db.Column(db.String(80), unique=False, nullable=False)
    # re-define what is shown when you print the class instance
    def __repr__(self):
        return '<Dog %r>' % self.animal_name


# create the database
db.create_all()

# create some users
def add_users():
    # users being created in the form of class instances
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    # adding both users to the session
    db.session.add(admin)
    db.session.add(guest)
    # committing the session changes to the database
    db.session.commit()
    return True

def add_animal():
    # users being created in the form of class instances
    freddy = Animal(animal_name='freddy', animal_type='dog', animal_breed='boxer')
    # adding both users to the session
    db.session.add(freddy)
    # committing the session changes to the database
    db.session.commit()
    return True


# add_animal()
# delete(Animal).where(User.username == 'freddy')


# retrieve all users
someuser = User.query.all()
# find a specific user
search_user = Animal.query.filter_by(animal_name='freddy').first()
print(search_user)

# create an inspector from the current engine
inspector = inspect(db.engine)
print(inspector.get_table_names())