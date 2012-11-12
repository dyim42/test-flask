# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Integer
from flask import g

SQLABase = declarative_base()

class Author(SQLABase):
    __tablename__   = 'author'
    id              = Column(Integer, primary_key = True, autoincrement = True)
    name            = Column(String(length=100))

    def __repr__(self):
        return "\n%s\n<Author entry(id: '%s', name: '%s')>\n%s\n" % \
            ('*'*80, self.id, self.name.encode('utf-8'), '*'*80)

    @classmethod
    def query_db(cls):
        """ Method returns SQLA Query object. """
        return g.db.query(cls)

class Book(SQLABase):
    __tablename__   = 'book'
    id              = Column(Integer, primary_key = True, autoincrement = True)
    name            = Column(String(length=200))

    def __repr__(self):
        return "\n%s\n<Book entry(id: '%s', name: '%s')>\n%s\n" % \
            ('*'*80, self.id, self.name.encode('utf-8'), '*'*80)

    @classmethod
    def query_db(cls):
        """ Method returns SQLA Query object. """
        return g.db.query(cls)

