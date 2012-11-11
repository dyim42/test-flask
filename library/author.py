# -*- coding: utf-8 -*-

# from python
import md5

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, current_app

# from app
import forms, models

# define blueprint
author = Blueprint('author', __name__, template_folder='templates')


@author.route('/', methods=['GET'])
def index():
    """ Index page. """
    return redirect(url_for('author.lst'))


@author.route('/create_form', methods=['GET'])
def create_form():
    """ Function renders author create form. """
    form = forms.Author()
    form.process()
    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('author_create.html', **context)


@author.route('/create', methods=['POST'])
def create():
    """ Function performs author create. """
    form = forms.Author()
    form.process(request.form)
    if form.validate():
        # make new entry
        _author = models.Author()
        form.populate_obj(_author)
        g.db.add(new_author)
        g.db.flush()
        # inform that it`s all OK
        return 'OK'

    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('author_create.html', **context)


@author.route('/list', methods=['GET'])
def lst():
    """ Function renders users list. """
    authors = models.Author.query_db().all()
    context = {
        'authors': authors,
    }
    return render_template('author_lst.html', **context)


@author.route('/update_form/<int:id>', methods=['GET'])
def update_form(id):
    """ Function renders author update page. """
    _author = models.Author.query_db().get(id)
    form = forms.Author()
    form.process(obj=_author)
    context = {
        'author' : _author,
        'action': 'update',
        'form': form,
    }
    return render_template('author_create.html', **context)


@author.route('/update/', methods=['POST'])
def update():
    """ Function updates author. """
    _author = models.Author.query_db().get(request.form['id'])
    form = forms.Author()
    form.process(request.form)
    if form.validate():
        form.populate_obj(_author)
        g.db.add(_author)
        g.db.flush()
        # inform front-end that it`s all OK
        return 'OK'

    context = {
        'author' : _author,
        'action': 'update',
        'form': form,
    }
    return render_template('author_create.html', **context)


@author.route('/delete/', methods=['POST'])
def delete():
    """ Function deletes author. """
    _author = models.Author.query_db().get(request.form['id'])
    g.db.delete(_author)
    g.db.flush()
    # inform front-end that it`s all OK
    return 'OK'


