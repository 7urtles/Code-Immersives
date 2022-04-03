from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def jinja_usage():
    return render_template('jinja_usage.html', item=something)


def something():
    return 'A thing'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)