"""
Below is an example of calling a template with kwargs
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def flask_kwargs():
    some_list = [
        'test',
        'thing',
        'brains', 
        'elbows'
     ]
    return render_template('jinja_usage.html', items=some_list)

app.run(host='0.0.0.0', port=5007)