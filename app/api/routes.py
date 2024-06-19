from flask import render_template, redirect, url_for, request, Blueprint
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content

# 'main' Blueprint 생성
api = Blueprint('api', __name__, template_folder='templates')

@api.route('/')
def test():
    return render_template('test.html')