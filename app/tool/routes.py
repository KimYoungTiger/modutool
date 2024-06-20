from flask import render_template, redirect, url_for, request, Blueprint
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content
import urllib.request
from . import tool
from ..services import perform_search

@tool.route('/search-ranking-product', methods=['GET', 'POST'])
def search_ranking_product():
    results = None
    search_initiated = False
    
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        store_name = request.form.get('store_name')
        search_sort = request.form.get('search_sort')
        # 검색 처리 로직 구현
        results = perform_search(search_query, store_name, search_sort)  # 실제 검색 함수 호출
        search_initiated = True
    
    return render_template('tool/search_ranking_product.html', results=results, search_initiated=search_initiated)
