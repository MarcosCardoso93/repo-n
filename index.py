from flask import Flask,render_template, request, session, make_response
import pymysql

app = Flask(__name__)
app.debug = True

db = pymysql.connect(host="localhost",user="root",password="",database="")

app.secret_key = "smakonakl0ioe8390732890dshui"

@app.route("/", methods=['GET' , 'POST' ])
def hello_world():
    if request.method == "GET":
        session['usuario'] = "Guilherme"
        return session['usuario']
    else:
        #request.form['nome'],
        return "O que veio do meu form: "+request. form[ 'conteudo' ]
    

@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: "+noticia_slug


if __name__ == '__main__':
    app.run()