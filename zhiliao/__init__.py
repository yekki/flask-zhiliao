# -*- coding: utf-8 -*-

from flask import Flask
from zhiliao import config
from zhiliao.exts import db, bootstrap
from zhiliao.auth import auth
from zhiliao.main import main

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
bootstrap.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(main)
