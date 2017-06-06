__author__ = 'jun.wen'

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class ReqForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class ReqFormV1(FlaskForm):
    url = StringField('please enter the URL: ', validators=[DataRequired()])
    submit =  SubmitField("Send")
    result = TextAreaField("Result: ")