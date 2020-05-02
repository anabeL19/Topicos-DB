from flask import Flask,render_template,request
from LemmaStems import *


app = Flask(__name__)

@app.route('/lemma_stems')
def index_lem_stemm():
    return render_template("template_ls.html")

@app.route('/lemma_stems',methods=['POST'])
def lema_stemm():
    content= request.form["plaintext"]
    
    if(request.form["opcion"]=="Lemma"):
        return render_template("template_ls.html", content=Lemmatization(content),inicial=content)
        
    else:
        return render_template("template_ls.html",content=Stemming(content),inicial=content)
        