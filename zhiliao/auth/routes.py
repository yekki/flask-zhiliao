# -*- coding: utf-8 -*-

from flask import session, redirect, url_for, flash, render_template, request
from zhiliao.exts import db
from zhiliao.auth import auth
from zhiliao.auth.forms import LoginForm, RegisterForm
from zhiliao.auth.models import User


@auth.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        phone_number = form.phone_number.data
        password = form.password.data
        user = User.query.filter(User.phone_number == phone_number, User.password == password).first()

        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('main.home'))
        else:
            flash('用户名或密码错误，请确认后再登录！', 'error')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        phone_number = request.form.get('phone_number')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        user = User(phone_number=phone_number, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        form.flash_errors()
        return render_template('register.html', form=form)
