"""
Below is an example of calling a template with kwargs
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def flask_kwargs():
    some_dictionary = {
        'thing':3,
        'another':4,
        'something':6,
        'thing2':8
    }
    return render_template('jinja_usage.html', **some_dictionary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)