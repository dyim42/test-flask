# -*- coding: utf-8 -*-
# from python
import md5

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, current_app

# from app
import forms, models
from lib.textfunct import md5x2

# define blueprint
profile = Blueprint('profile', __name__, template_folder='templates')

PSWD_substitute = 'password_was_not_changed'

@profile.route('/', methods=['GET'])
def index():
    """ Current user profile page. """
    return redirect(url_for('profile.lst'))


@profile.route('/create_form', methods=['GET'])
def create_form():
    """ Function renders profile creation form. """
    form = forms.Profile()
    form.process()
    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('profiles_create.html', **context)


@profile.route('/create', methods=['POST'])
def create():
    """ Function performs user creation. """
    form = forms.Profile()
    form.process(request.form)
    if form.validate():
        # get password hash
        salt = current_app.config['PASSWORD_SALT']
        password_hash = md5x2(form.password.data, salt)

        # make new entry
        _profile = models.Profile()
        form.populate_obj(_profile)
        _profile.passwd = password_hash
        g.db.add(_profile)
        g.db.flush()
        # inform that it`s all OK
        return 'OK'

    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('profiles_create.html', **context)


@profile.route('/list', methods=['GET'])
def lst():
    """ Function renders users list. """
    profiles = models.Profile.users()
    form = forms.Profile()
    context = {
        'profiles': profiles,
        'form': form,
    }
    return render_template('profiles_lst.html', **context)


@profile.route('/update_form/<int:id>', methods=['GET'])
def update_form(id):
    """ Function renders user`s profile update page. """
    _profile = models.Profile.query_db().get(id)
    if not _profile: abort(404)

    form = forms.Profile()
    form.process(obj=_profile)
    form.password.data = PSWD_substitute
    form.confirm_password.data = PSWD_substitute
    context = {
        'profile' : _profile,
        'action': 'update',
        'form': form,
    }
    return render_template('profiles_create.html', **context)


@profile.route('/update/', methods=['POST'])
def update():
    """ Function updates user profile. """
    id = int(request.form['id'])
    _profile = models.Profile.query_db().get(id)
    if not _profile: abort(404)
    form = forms.Profile()
    form.process(request.form)

    if form.validate():
        salt = current_app.config['PASSWORD_SALT']
        old_password_hash = _profile.passwd
        new_password_hash = md5x2(form.password.data, salt)
        # update entry
        form.populate_obj(_profile)
        if form.password.data == PSWD_substitute:
            _profile.passwd = old_password_hash
        else:
            _profile.passwd = new_password_hash

        g.db.add(_profile)
        g.db.flush()
        # inform front-end that it`s all OK
        return 'OK'

    context = {
        'profile' :_profile,
        'action': 'update',
        'form': form,
    }
    return render_template('profiles_create.html', **context)


@profile.route('/delete/', methods=['POST'])
def delete():
    """ Function deletes user`s profile. """
    if not profile.has_access(): abort(403)
    id = int(request.form['id'])
    _profile = models.Profile.query_db().get(id)
    if not _profile: abort(404)

    g.db.delete(_profile)
    g.db.flush()
    return 'OK'


