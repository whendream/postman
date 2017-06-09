__author__ = 'jun.wen'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ReqFormV1(FlaskForm):
    #method = SelectField(choices=[('wm-api', 'biz-api', "other")])
    method = SelectField(u'Method', choices=[('get', 'GET'), ('post', 'POST'), ('delete', 'DELETE')])
    url = StringField('Please enter the URL: ', validators=[DataRequired()])
    reqBody = TextAreaField("Request Body: ",render_kw={'class':'text-body','rows':15})
    submit = SubmitField("Send")
    result = TextAreaField("Result: ",render_kw={'class':'text-body','rows':20})


class SimpleForm(FlaskForm):
    action = SelectField(u'请选择场景', choices=[('get', '根据wm_people_id查看自媒体人信息'), ('post', '根据article_id查看文章信息'), ('delete', 'TODO')])
    keyword = StringField(u'请根据场景输入关键字段', validators=[DataRequired()])
    submit = SubmitField("Send")
    result = TextAreaField("Result: ",render_kw={'class':'text-body','rows':20})