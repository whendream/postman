__author__ = 'jun.wen'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class ReqForm(Form):
    url = StringField('url', validators=[DataRequired()])