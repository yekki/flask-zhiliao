# -*- coding: utf-8 -*-

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from zhiliao.exts import BaseForm


class QuestionForm(BaseForm):
    title = StringField('标题', validators=[DataRequired(), Length(min=1, max=99, message='请确认标题小于99个字符')])
    content = TextAreaField('内容', validators=[DataRequired()])
    submit = SubmitField('提交')


class CommentForm(BaseForm):
    content = TextAreaField('内容', validators=[DataRequired()])
    question_id = StringField('question_id')
    submit = SubmitField('提交评论')
