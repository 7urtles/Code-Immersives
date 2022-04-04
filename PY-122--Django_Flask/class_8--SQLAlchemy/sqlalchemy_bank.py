from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

## commenting out after first run to avoid errors/multiple entries..im lazy
# add_users()

# to update a row value (an Account instance in the database)
# first query the desired row (Account)
user_to_change = Account.query.filter(Account.firstname == 'Dave').first()

# second, update the queried instances value to update the database
user_to_change.lastname = 'changed'
all_users = Account.query.all()

# Syntax for conditionals in queries.. Normal python style
someuser = Account.query.filter(Account.initial_amount >= 2000).all()

# ----deleting an account----
Account.query.filter(Account.firstname == 'Dave').delete()
db.session.commit()

print(user_to_change)
print(all_users)