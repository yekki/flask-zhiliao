# -*- coding: utf-8 -*-8

from flask import Flask
from flask import render_template, request, session, redirect, url_for
from decorators import login_required
from exts import db
from models import User, Question, Comment

import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def home():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/detail/<question_id>')
def detail(question_id):
    question = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question)


@app.route('/comment/', methods=['POST'])
@login_required
def comment():
    question_id = request.form.get('question_id')
    comment = Comment(content=request.form.get('content'))
    comment.author = User.query.filter(User.id == session.get('user_id')).first()
    comment.question = Question.query.filter(Question.id == question_id).first()

    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        user = User.query.filter(User.phone_number == phone_number, User.password == password).first()

        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('home'))
        else:
            return '用户名或密码错误，请确认后再登录！'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone_number = request.form.get('phone_number')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        user = User.query.filter(User.phone_number == phone_number).first()
        if user:
            return '该手机号码已经被注册了，请更换手机号码！'
        else:
            if password != confirm:
                return '两次密码不一致，请确认后再填写！'
            else:
                user = User(phone_number=phone_number, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.context_processor
def context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()
