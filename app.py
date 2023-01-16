from flask import Flask, render_template, request, flash
from util import *
import json


app= Flask(__name__)
app.secret_key = "lll"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST","GET"])
def search():
    output,listOfweb,username= main(request.form['name_input'])
    return render_template("result.html",result=output,webList=listOfweb,user=username)
    
if __name__=="__main__":
    app.run(debug=True)             