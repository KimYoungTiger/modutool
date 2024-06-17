from flask import Flask
from config import Config
from .extensions import db, migrate
from .main import main as main_blueprint
from .auth import auth as auth_name_blueprint
from .api import api as api_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # 에러 핸들링
    @app.errorhandler(404)
    def not_found_error(error):
        return "Page not found", 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return "Internal server error", 500

    # Blueprint 등록
    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(auth_name_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
