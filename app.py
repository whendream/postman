__author__ = 'jun.wen'

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myform import ReqForm
from getResponse import getReq

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')

@app.route("/postman" , methods = ['GET', 'POST'])
def show():
    form = ReqForm()
    if form.validate_on_submit():
        result = getReq(form.url.data)
        return render_template('postman.html',form = form,result=result)
    return render_template('postman.html',form = form,result="null")

if __name__ == "__main__":
    app.run(debug=True)