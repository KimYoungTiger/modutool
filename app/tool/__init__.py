from flask import Blueprint

tool = Blueprint('tool', __name__, template_folder='templates/tool')

from . import routes

