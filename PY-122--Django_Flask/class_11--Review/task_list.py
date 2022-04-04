from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy

# make a flask application that takes input from an html page,
# and saves it to a sqlalchemy database

app = Flask(__name__)

# specify database engine and database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# create a database session instance
db = SQLAlchemy(app)

# defining database Task table structure
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), nullable=False)
    task_details = db.Column(db.String(50), nullable=False)

# create database and tables if they don't exist
db.create_all()


# at the home route....
@app.route('/')
def home():
    # show the html task creation form
    return render_template('index.html', tasks=get_all_tasks())


# route receiving the form submission. Route is specified on the html form submit action
# make sure the routes method matches the html forms request type
@app.route('/create', methods=['POST'])
def submit_task():
    # grab data from the received post request and store it
    task_name = request.form['task_name']
    task_details = request.form['task_details']
    # creating a dict of the received data
    new_task = {
        'task_name':task_name,
        'task_details':task_details
    }
    # send dict to the task creation function
    create_task(new_task)
    # return the 'success' template and display the created task details
    return redirect(request.referrer)


@app.route('/delete', methods=['POST'])
def delete_task():
    # grab data from the received post request and store it
    task_id = request.form['task_id']
    Task.query.filter(Task.id == task_id).delete()
    db.session.commit()
    return redirect(request.referrer)



# adds tasks to the database
def create_task(new_task:dict) -> Task:
    task = Task(**new_task)
    # use add_all() to add the list of Accounts
    db.session.add(task)
    # commit changes to database
    db.session.commit()
    return task

def get_all_tasks() -> list:
    tasks = Task.query.all()
    return tasks

app.run(host='0.0.0.0',port=5007)