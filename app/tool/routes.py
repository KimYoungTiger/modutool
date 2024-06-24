from flask import render_template, redirect, url_for, request, Blueprint
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content
from . import tool
import app.services

@tool.route('/search-ranking-mystore', methods=['GET', 'POST'])
def search_ranking_mystore():
    results = None
    search_initiated = False
    
    if request.method == 'POST':

        search_query = request.form.get('search_query')
        store_name = request.form.get('store_name')
        search_sort = request.form.get('search_sort')
            
        # 검색 처리 로직 구현
        results = app.services.perform_search_ranking_mystore(search_query, store_name, search_sort)  # 실제 검색 함수 호출
        search_initiated = True
        
    return render_template('tool/search_ranking_mystore.html', results=results, search_initiated=search_initiated)

@tool.route('/list-product', methods=['GET', 'POST'])
def list_product():
    results = None
    search_initiated = False
    
    if request.method == 'POST':
        store_name = request.form.get('store_name')
        search_sort = request.form.get('search_sort')
        search_count = request.form.get('search_count')
        # 검색 처리 로직 구현
        results = app.services.perform_list_product(store_name, search_sort, search_count)  # 실제 검색 함수 호출
        search_initiated = True
    
    return render_template('tool/list_product.html', results=results, search_initiated=search_initiated)


@tool.route('/search-ranking-store', methods=['GET', 'POST'])
def search_ranking_store():
    results = None
    search_initiated = False
    
    if request.method == 'POST':

        search_query = request.form.get('search_query')
        search_sort = request.form.get('search_sort')
        search_count = request.form.get('search_count')
            
        # 검색 처리 로직 구현
        results = app.services.perform_search_ranking_store(search_query, search_sort, search_count)  # 실제 검색 함수 호출
        search_initiated = True
        
    return render_template('tool/search_ranking_store.html', results=results, search_initiated=search_initiated)


@tool.route('/search-keyword', methods=['GET', 'POST'])
def search_keyword():
    results = None
    search_initiated = False
    
    return render_template('tool/search_keyword.html', results=results, search_initiated=search_initiated)