from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index(): # essa função poderia ter qualquer nome
	return render_template("index.html") 

# para retornar um template que deve estar dentro da pasta templates

@app.route("/var")
def var(): # essa função poderia ter qualquer nome
	names = ["alex", "pamela", "mayco"]
	v = ['1', '2' ,'3']
	return render_template("index.html", names=names) 

@app.route("/vrau", methods=["POST"]) # criando uma rota que aceita apenas o método post
def vrau():
	num1 = int(request.form.get("num1")) # pegando o valor do form pelo name
	num2 = int(request.form.get("num2")) # utilizando a função int para converter para inteiro
	result = num1 + num2
	return render_template("hello.html", result=result) # render template recebe como argumento o arquivo html e as variáveis que serão impressas
