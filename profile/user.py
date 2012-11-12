# -*- coding: utf-8 -*-

# from python

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, session, current_app, flash

# from app
import forms,  models
from lib.textfunct import md5x2

# define blueprint
user = Blueprint('user', __name__, template_folder='templates')


@user.route('/login', methods=['POST'])
def login():
    """Logs the user in."""
    
    login = request.form.get('email')
    password = request.form.get('password')
    profile = models.Profile.get_by_email(login)
    
    if not login or not password or not profile:
        flash('Incorrect login/password')
        return redirect(request.referrer)
    salt = current_app.config['PASSWORD_SALT']
    password_hash = md5x2(password, salt)
    if profile.passwd != password_hash:
        flash('Incorrect login/password')
        return redirect(url_for('profiles.lst'))

    session['user_id'] = profile.id
    session['is_authenticated'] = True

    return redirect(request.referrer)


@user.route('/logout')
def logout():
    """Logs the user out."""
    session['user_id'] = models.Profile.get_anonymous().id
    session['is_authenticated'] = False

    return redirect(url_for('index'))

def has_access():
    if g.user.name == 'anonymous': return False
    return True


