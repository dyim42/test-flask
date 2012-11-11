# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer, Date
from flask import g

SQLABase = declarative_base()

class Profile(SQLABase):
    __tablename__   = 'profile'
    id              = Column(Integer, primary_key = True, autoincrement = True)
    # Account info
    name            = Column(String(length=50))
    email           = Column(String(length=100), unique=True)
    about           = Column(String(length=1000))
    passwd          = Column(String(length=32))

    birthday        = Column(Date)

    def __repr__(self):
        return "\n%s\n<Profile entry(id: '%s', email: '%s')>\n%s\n" % \
            ('*'*80, self.id, self.email, '*'*80)

    @classmethod
    def get_by_email(cls, email):
        try:
            return g.db.query(cls).filter_by(email=email)[0]
        except IndexError:
            return None

    @classmethod
    def get_anonymous(cls):
        try:
            return g.db.query(cls).filter_by(email='anonymous')[0]
        except:
            raise Exception('There is no any anonymous user in system!')

    @classmethod
    def users(cls):
        query = g.db.query(cls).filter(cls.email != 'anonymous')
        return query.all()

    @classmethod
    def query_db(cls):
        """ Method returns SQLA Query object. """
        return g.db.query(cls)