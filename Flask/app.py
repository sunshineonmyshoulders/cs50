from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): # essa função poderia ter qualquer nome
	return render_template("index.html") 

# para retornar um template que deve estar dentro da pasta templates

@app.route("/var")
def var(): # essa função poderia ter qualquer nome
	vrau = "KKKKKKJ"
	return render_template("index.html", headline=vrau) 

