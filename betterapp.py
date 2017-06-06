#coding=utf-8
'''
Created on 2017年6月5日

@author: jun.wen
'''
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myform import ReqFormV1

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

@app.route("/")
def index():
    form = ReqFormV1()
    return render_template("index.html",form = form)


if __name__=="__main__":
    app.run()