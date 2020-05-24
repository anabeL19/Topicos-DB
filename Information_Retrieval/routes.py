from flask import Flask,render_template,request
from modelo_binario import *


app = Flask(__name__)

@app.route('/info_recover')
def index_lem_stemm():
    return render_template("info_recover.html")

@app.route('/info_recover',methods=['POST'])
def lema_stemm():
    content= request.form["plaintext"]
    
    if(request.form["opcion"]=="Search"):
        return render_template("info_recover.html", content=row_word(content),inicial=content)
        
    # else:
    #     return render_template("info_recover.html",content=Stemming(content),inicial=content)