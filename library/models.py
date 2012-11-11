# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer
from flask import g

SQLABase = declarative_base()

class Author(SQLABase):
    __tablename__   = 'author'
    id              = Column(Integer, primary_key = True, autoincrement = True)
    # Account info
    name            = Column(String(length=50))

    def __repr__(self):
        return "\n%s\n<Profile entry(id: '%s', name: '%s')>\n%s\n" % \
            ('*'*80, self.id, self.name.encode('utf-8'), '*'*80)

    @classmethod
    def query_db(cls):
        """ Method returns SQLA Query object. """
        return g.db.query(cls)
