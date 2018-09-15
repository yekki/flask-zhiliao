# -*- coding: utf-8 -*-

from zhiliao.exts import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    phone_number = db.Column(db.String(13), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
