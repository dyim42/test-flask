# -*- coding: utf-8 -*-
from wtforms import Form, fields, validators

class Profile(Form):
    name        = fields.TextField(u'Name', [validators.Optional(), validators.length(min = 3, max = 50)])
    email       = fields.TextField(u'Email', [validators.Required(), validators.length(max = 100), validators.Email()])

    birthday    = fields.DateField(u'Birth day', [validators.Optional(),], format='%Y %d %m')
    about       = fields.TextAreaField(u'About', [validators.Optional(), validators.length(max=1000)])

    password    = fields.PasswordField(u'Password', [validators.Required(), validators.length(min=8)])
    confirm_password    = fields.PasswordField(u'Confirm Password', [validators.Required(), validators.EqualTo('password', message='Passwords must match')])
