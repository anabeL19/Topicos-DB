from flask import Flask,render_template,request
from boolean_model import *


app = Flask(__name__)

@app.route('/info_recover')
def index_lem_recover():
    return render_template("info_recover.html")

@app.route('/info_recover',methods=['POST'])
def info_recover():
    content= request.form["plaintext"]
    
    if(request.form["option"]=="Search"):
        return render_template("info_recover.html", content=show(content),inicial=content)
        