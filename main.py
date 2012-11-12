# -*- coding: utf-8 -*-
# from python imports

# from flask imports
from flask import Flask, Blueprint, g, request, session, redirect, url_for


from werkzeug.datastructures import MultiDict
from werkzeug.wrappers import BaseRequest
BaseRequest.parameter_storage_class = MultiDict


# create application
app = Flask(__name__)
app.config.from_object('settings')
app.debug = app.config['DEBUG']

def javascrpt_escape(value):
    value = r'\n'.join(value.splitlines())
    value = value.replace("'", r"\&#39;").replace('"', r'\&#34;')
    return value

app.jinja_env.filters['js_e'] = javascrpt_escape

from profile.user import has_access
app.jinja_env.globals['has_access'] = has_access
Blueprint.has_access = has_access

from lib.redis_session import RedisSessionInterface
app.session_interface = RedisSessionInterface()

# Blueprints
from profile.profile import profile
app.register_blueprint(profile, url_prefix='/profile')
from profile.user import user
app.register_blueprint(user, url_prefix='/user')


from library.author import author
app.register_blueprint(author, url_prefix='/authors')
from library.book import book
app.register_blueprint(book, url_prefix='/book')
from library.search import search
app.register_blueprint(search, url_prefix='/search')


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Open connection to DB
SQLAlchemy_engine = create_engine('sqlite:///' + app.config['DATABASE'],
    encoding='utf-8',
    echo = not app.config['SILENT']
)
SQLA_session = sessionmaker(bind=SQLAlchemy_engine, autoflush=False)


from profile.models import Profile as profile_model


@app.before_request
def before_request():
    # Begin transaction
    g.db = SQLA_session()
    g.user = profile_model.query_db().get(session['user_id'])


@app.after_request
def after_request(response):
    # Commit transaction
    g.db.commit()
    return response


@app.teardown_request
def teardown_request(exception):
    # Rollback transaction
    g.db.rollback() 

@app.route('/')
def index():
    return redirect(url_for('profile.lst'))

# Run application
if __name__ == '__main__':
    app.run()

