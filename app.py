from flask import Flask, render_template, request, flash
from util import *
import json


app= Flask(__name__)
app.secret_key = "lll"


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/loading", methods=["POST"])
# def loading():
#     return render_template("loading.html")

@app.route("/result", methods=["POST","GET"])
def search():
    # output,listOfweb,username,names,risk= main(request.form['name_input'])
    x= request.form['name_input']
    output,listOfweb,username,names= test()
    # return render_template("result.html",result=output,webList=listOfweb,user=username,name=names,level = risk)
    return render_template("result.html",result=output,webList=listOfweb,user=username,name=names)

if __name__=="__main__":
    app.run(debug=True)             