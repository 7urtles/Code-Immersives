from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5500)
    server = Server(app.wsgi_app)
    server.serve(port=5500, host='0.0.0.0')