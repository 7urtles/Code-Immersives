"""
Learning sqlAlchemy and implementation with flask
"""

from flask import Flask
from sqlalchemy import create_engine, MetaData, Table


app = Flask(__name__)


engine = create_engine('sqlite:////tmp/test.db',echo=True)
metadata = MetaData(bind=engine)
users = Table('users', metadata, autoload=True)
metadata.create_all(engine)


con = engine.connect()
con.execute(users.insert(), name='admin', email='admin@localhost')


@app.route('/sqlalchemy')
def using_sqlalchemy():
    return 'some bullshit'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)