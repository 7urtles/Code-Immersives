"""
Flask app to display server hosts username
"""


from flask import Flask, render_template
import getpass
app = Flask(__name__)


@app.route('/username')
def get_user():
    return render_template('username.html', username_function=getpass.getuser)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)