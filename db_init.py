from __future__ import with_statement
from settings import DATABASE
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
import os

def init_db():
    with closing(sqlite3.connect(DATABASE)) as db:
        with open('schema.sql') as f:
            line = f.read()
            db.cursor().executescript(line)
        db.commit()

if __name__ == '__main__':
    init_db()
