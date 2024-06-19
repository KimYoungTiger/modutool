from flask import render_template, redirect, url_for, request, Blueprint
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content
from . import tool

@tool.route('/searching', methods=['GET', 'POST'])
def searching():
    results = None
    search_initiated = False
    
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            results = Content.query.filter(Content.title.contains(search_query)).all()
            search_initiated = True
            
    return render_template('tool/searching.html', results=results, search_initiated=search_initiated)