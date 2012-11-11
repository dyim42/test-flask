# -*- coding: utf-8 -*-
# from python imports
# from flask imports
from flask import Flask, g

# create application
app = Flask(__name__)
app.config.from_object('settings')
app.debug = app.config['DEBUG']

from lib.redis_session import RedisSessionInterface
app.session_interface = RedisSessionInterface()

# Blueprints
from profile import profile
app.register_blueprint(profile.profile, url_prefix='/profile')
from library import author
app.register_blueprint(author.author, url_prefix='/authors')
#from library import books
#pp.register_blueprint(books.book, url_prefix='/book')


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Open connection to DB
SQLAlchemy_engine = create_engine(app.config['DATABASE'],
    encoding='utf-8',
    echo = True
)
SQLA_session = sessionmaker(bind=SQLAlchemy_engine, autoflush=False)

@app.before_request
def before_request():
    # begin transaction
    g.db = SQLA_session()

    # authentication without authorization by technical task policy
#    if user.authentication.is_user():
#        user.authentication.user_to_g()
#    else:
#        user.authentication.logout()


@app.after_request
def after_request(response):
    # commit transaction
    g.db.commit()
    return response


@app.teardown_request
def teardown_request(exception):
    # rollback transaction
    g.db.rollback() 
    # and here is the place to email an exception to developer


# run application
if __name__ == '__main__':
#    app.run('192.168.1.100', 5000)
    app.run()

