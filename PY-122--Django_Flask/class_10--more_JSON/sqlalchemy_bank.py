from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from random import randint


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'

db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    account_number = db.Column(db.Integer, nullable=False, unique=True)
    initial_amount = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname} {self.account_number}"

db.create_all()

Charles = {
    'firstname':'Charles',
    'lastname':'Parmley',
    'account_number':randint(10000,99999),
    'initial_amount':50
}
Dave = {
    'firstname':'Dave',
    'lastname':'Davidson',
    'account_number':randint(10000,99999),
    'initial_amount':randint(0,2000)
}
Bill = {
    'firstname':'Bill',
    'lastname':'Bronson',
    'account_number':randint(10000,99999),
    'initial_amount':randint(0,2000)
}
Christina = {
    'firstname':'Christina',
    'lastname':'Bronson',
    'account_number':randint(10000,99999),
    'initial_amount':1000
}
def add_users():
    # creating Account class instances
    user1 = Account(**Charles)
    user2 = Account(**Dave)
    user3 = Account(**Bill)
    user4 = Account(**Christina)
    # stuff em in a list
    new_users = [user1,user2,user3,user4]
    # use add_all() to add the list of Accounts
    db.session.add_all(new_users)
    # commit changes to database
    db.session.commit()
    return True

# A query to see if there are any users in the database
user_to_change = Account.query.filter(Account.id == 1).first()
# if accessing the id of the query result fails,
#  that means there are no users created yet
try: user_to_change.id
# so create them
except: add_users()

