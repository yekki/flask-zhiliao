# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, session, url_for
from zhiliao.main import main
from zhiliao.main.models import Question, Comment
from zhiliao.auth.models import User
from zhiliao.main.forms import CommentForm, QuestionForm
from zhiliao.exts import db, login_required


@main.route('/')
def home():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@main.route('/detail/<question_id>')
def detail(question_id):
    question = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question, form=CommentForm())


@main.route('/comment/', methods=['POST'])
@login_required
def comment():
    question_id = request.form.get('question_id')
    comment = Comment(content=request.form.get('content'))
    comment.author = User.query.filter(User.id == session.get('user_id')).first()
    comment.question = Question.query.filter(Question.id == question_id).first()

    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.detail', question_id=question_id))


@main.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    form = QuestionForm()

    if form.validate_on_submit():
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
        form.flash_errors()
        return render_template('question.html', form=form)


@main.context_processor
def context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}
