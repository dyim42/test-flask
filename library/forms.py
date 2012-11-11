# -*- coding: utf-8 -*-
from wtforms import Form, fields, validators

class Author(Form):
    name        = fields.TextField(u'Name', [validators.Required(), validators.length(max = 100)])

