# -*- coding: utf-8 -*-

# from python

# from flask
from flask import Blueprint, render_template, g, request, redirect, url_for, abort, current_app

# from app
import models

# define blueprint
search = Blueprint('search', __name__, template_folder='templates')

@search.route('/', methods=['GET', 'POST'])
@search.route('/<query>', methods=['GET'])
def perform_search(query=''):
    if request.method == 'GET':
        search_str = query
    elif request.method == 'POST':
        search_str = request.form.get('query')
    if not search_str:
        return render_template('search_lst.html', **dict())
    

    authors = models.Author.query_db().filter(models.Author.name.like('%' + search_str + '%')).all()
    books = models.Book.query_db().filter(models.Book.name.like('%' + search_str + '%')).all()
    context = {
        'authors' : authors,
        'books' : books    
    }
    return render_template('search_lst.html', **context)

