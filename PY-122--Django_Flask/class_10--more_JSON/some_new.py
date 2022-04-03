from sqlalchemy_bank import app, Account

def get_user(id):
    return Account.query.filter(Account.id == id).all()

@app.route('/')
def thing():
    return 'the home page works'

@app.route('/<id>')
def find_user(id):
    user = get_user(id)
    if user: return f"{user}"
    return 500

@app.errorhandler(500)
def error500(id):
    return 'error 500',500

@app.errorhandler(404)
def error404(id):
    return 'error 404',404

app.run(host='0.0.0.0', port=5007)