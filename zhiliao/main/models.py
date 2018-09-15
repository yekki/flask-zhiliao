# -*- coding: utf-8 -*-

from datetime import datetime
from zhiliao.exts import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('questions'))

    def __repr__(self):
        return f'<Question {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    question = db.relationship('Question', backref=db.backref('comments', order_by=(id.desc())))
    author = db.relationship('User', backref=db.backref('comments'))

    def __repr__(self):
        return f'<Comment {self.content}>'
