"""
Key word arguments with flask INCOMPLETE
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/kwargs')
def using_kwargs():
    return render_template('kwargs.html', someshit='shit')

app.run(host='0.0.0.0', port=5007)