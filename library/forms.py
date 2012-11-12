# -*- coding: utf-8 -*-
from wtforms import Form, fields, validators

import models
class Author(Form):
    name = fields.TextField(u'Name', [validators.Required(), validators.length(max = 100)])
    books_mtm = fields.SelectMultipleField(u'Books')

    def __init__(self, author = None, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        books = models.Book.query_db().all()
        self.books_mtm.choices = ((unicode(x.id), x.name) for x in books)
        if author:
            self.books_mtm.default = (unicode(x.id) for x in author.books)
        

class Book(Form):
    name = fields.TextField(u'Name', [validators.Required(), validators.length(max = 200)])

