# -*- coding: utf-8 -*-

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length, Regexp
from zhiliao.exts import BaseForm
from zhiliao.auth.models import User


class LoginForm(BaseForm):
    phone_number = StringField('手机号码')
    password = PasswordField('密码')
    submit = SubmitField('登录')


class RegisterForm(BaseForm):
    phone_number = StringField('手机号码', validators=[DataRequired('请输入手机号'), Regexp("1[3578]\d{9}", message="手机格式不正确")])
    password = PasswordField('密码', validators=[DataRequired('请输入密码'), Length(min=6, max=10, message='密码6~10个字符')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='密码必须一致')])
    username = StringField('用户名', validators=[DataRequired('请输入用户名')])
    submit = SubmitField('登录')

    def validate_phone_number(self, field):
        user = User.query.filter(User.phone_number == field.data).first()
        if user:
            raise ValidationError('该手机号码已经被注册了，请更换手机号码！')
