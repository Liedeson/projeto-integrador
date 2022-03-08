from flask import render_template, request
from flask_sqlalchemy import SQLALchemy
from app import app


@app.route('/')
@app.route('/index')
def index():
    usuario = {"nome": "lili",  "tema": "Jogos educativos"}
    
    return render_template('index.html', usuario=usuario, titulo='Pagina inicial')
    
@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre")


@app.route('/login')
def login():
    return render_template('login.html')



    







