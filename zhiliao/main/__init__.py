# -*- coding: utf-8 -*-

from flask_bootstrap import Blueprint

main = Blueprint('main', __name__, url_prefix='/', static_folder='static', template_folder='templates')

from zhiliao.main.routes import *