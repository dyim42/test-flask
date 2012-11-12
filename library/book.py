# -*- coding: utf-8 -*-

# from python
import md5

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, current_app

# from app
import forms, models

# define blueprint
book = Blueprint('book', __name__, template_folder='templates')


@book.route('/', methods=['GET'])
def index():
    """ Index page. """
    return redirect(url_for('book.lst'))


@book.route('/create_form', methods=['GET'])
def create_form():
    """ Function renders book create form. """
    form = forms.Book()
    form.process()
    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('book_create.html', **context)


@book.route('/create', methods=['POST'])
def create():
    """ Function performs book create. """
    form = forms.Book()
    form.process(request.form)
    if form.validate():
        # make new entry
        _book = models.Book()
        form.populate_obj(_book)
        g.db.add(_book)
        g.db.flush()
        # inform that it`s all OK
        return 'OK'

    context = {
        'action': 'create',
        'form': form,
    }
    return render_template('book_create.html', **context)


@book.route('/list', methods=['GET'])
def lst():
    """ Function renders users list. """
    books = models.Book.query_db().all()
    context = {
        'books': books,
    }
    return render_template('book_lst.html', **context)


@book.route('/update_form/<int:id>', methods=['GET'])
def update_form(id):
    """ Function renders book update page. """
    _book = models.Book.query_db().get(id)
    form = forms.Book()
    form.process(obj=_book)
    context = {
        'book' : _book,
        'action': 'update',
        'form': form,
    }
    return render_template('book_create.html', **context)


@book.route('/update/', methods=['POST'])
def update():
    """ Function updates book. """
    _book = models.Book.query_db().get(request.form['id'])
    form = forms.Book()
    form.process(request.form)
    if form.validate():
        form.populate_obj(_book)
        g.db.add(_book)
        g.db.flush()
        # inform front-end that it`s all OK
        return 'OK'

    context = {
        'book' : _book,
        'action': 'update',
        'form': form,
    }
    return render_template('book_create.html', **context)


@book.route('/delete/', methods=['POST'])
def delete():
    """ Function deletes book. """
    if not profile.has_access(): abort(403)
    _book = models.Book.query_db().get(request.form['id'])
    g.db.delete(_book)
    g.db.flush()
    # inform front-end that it`s all OK
    return 'OK'


