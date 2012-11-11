# -*- coding: utf-8 -*-

# from python
import smtplib
from email.mime.text import MIMEText

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, session, current_app, flash

# from app
import forms
from lib.aa import authentication
from profile import models
from lib.textfunct import md5x2

# define blueprint
user = Blueprint('user', __name__, template_folder='templates')

'''
================================================================================
First line
================================================================================
    ( / or /login_form) - User login
    ( / or /login)      - User login
    (/logout)           - User logout

    (/register_form)    - Register form
    (/register)         - Perform register
    (/register_submit)  - Submit register
    (/register_refuse)  - Refuse register

    (/restore_form)
'''


@user.route('/', methods=['GET'])
@user.route('/login_form/', methods=['GET'])
def login_form():
    """Renders login form."""
    if g.user.logged_in(): return redirect(url_for(g.index_page))
    return render_template('aa/user_login.html')


@user.route('/login/', methods=['POST'])
def login():
    """Logs the user in."""
    login = request.form['login']
    password = request.form['password']
    profile = models.Profile.get_by_email(login)
    if not login or not password or not profile:
        flash('Incorrect login/password')
        return redirect(url_for('user.login_form'))

    salt = current_app.config['PASSWORD_SALT']
    password_hash = md5x2(password, salt)
    if profile.passwd != password_hash:
        flash('Incorrect login/password')
        return redirect(url_for('user.login_form'))

    authentication.login(profile)
    return redirect(url_for(g.index_page))


@user.route('/logout')
def logout():
    """Logs the user out."""
    if not g.user.logged_in(): return redirect(url_for('user.login_form'))
    authentication.logout()
    return redirect(url_for('user.login_form'))


@user.route('/register_form', methods=['GET'])
def register_form(form=None):
    """Renders register form page."""
    if not current_app.config.get('REGISTRATION_ENABLED'): abort(404)

    if g.user.logged_in():
        return redirect(url_for('profile.index'))

    if form is None:
        form = forms.RegisterCommonForm()

    context = {}
    context['form'] = form
    return render_template('aa/user_register.html', **dict())


@user.route('/register', methods=['POST'])
def register():
    """Renders register form page."""
    if not current_app.config.get('REGISTRATION_ENABLED'): abort(404)

    if g.user.logged_in():
        return redirect(url_for('profile.index'))

    form = forms.RegisterCommonForm()
    form.process(request.form)
    if form.validate():
        profile = models.Profile()
        form.populate_obj(profile)
        salt = current_app.config['PASSWORD_SALT']
        profile.passwd = md5x2(form.password.data, salt)
        profile.save()
        flash('You were successfully registered!')
        return redirect(url_for('user.login_form'))

    return register_form(form)






















@user.route('/restore_form', methods=['GET'])
def restore_form():
    """User password restoring form"""
    pass


@user.route('/restore/', methods=['POST'])
def restore():
    """Emails with token to user"""
    pass


@user.route('/process_restore/<token>', methods=['GET'])
def process_restore(token):
    """Emails with token to user"""
    pass
