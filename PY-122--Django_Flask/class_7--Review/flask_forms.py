from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('forms.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['user_name']
    password = request.form['user_password']
    message = request.form['user_message']
    return f"Username: {username} <br>Password: {password} <br>Message: {message}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)