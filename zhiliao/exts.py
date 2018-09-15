# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask import flash, session, redirect, url_for
from functools import wraps

db = SQLAlchemy()
bootstrap = Bootstrap()


class BaseForm(FlaskForm):
    def flash_errors(self):
        for field, errors in self.errors.items():
            for error in errors:
                flash(u"%s - %s" % (
                    getattr(self, field).label.text,
                    error
                ), 'error')


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))

    return wrapper
