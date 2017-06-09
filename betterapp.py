'''
Created on 2017年6月5日

@author: jun.wen
'''
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myform import ReqFormV1,SimpleForm
from getResponse import getReq

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = ReqFormV1()
    if form.validate_on_submit():
        result = getReq(form.url.data)
        print(form.method.data)
        return render_template('index.html',form = form,result=result)
    return render_template("index.html",form = form)

@app.route("/simple", methods = ['GET', 'POST'])
def simple():
    form = SimpleForm()
    if form.validate_on_submit():
        result = getReq(form.url.data)
        print(form.method.data)
        return render_template('simple.html',form = form,result=result)
    return render_template("simple.html",form = form)

if __name__=="__main__":
    app.run(debug=True)