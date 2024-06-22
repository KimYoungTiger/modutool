from flask import render_template, redirect, url_for, request, Blueprint
from authlib.integrations.flask_client import OAuth
from . import auth
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content
import app.services

oauth = OAuth()

google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

@auth.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorize_google', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/authorize/google')
def authorize_google():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # 여기서 user_info를 사용하여 사용자를 로그인 처리합니다.
    return redirect(url_for('main.profile'))
