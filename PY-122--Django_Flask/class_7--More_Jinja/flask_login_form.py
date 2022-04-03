from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit')
def check_login():
    # The username and password data are gathered from the <input> tags, within the html document
    # The 'name' argument within the input field is the exact name that needs to be passed to request.args.get()
    username  = request.args.get('username')
    password  = request.args.get('password')
    return f"{username}, {password}"

app.run(host='0.0.0.0', port=5007)