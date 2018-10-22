from flask import Flask

app = Flask(__name__) # cria uma variável

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/vrau") # criar uma rota é simples d+
def david():
        return "Hello, vrau"


@app.route("/<string:name>") # uma rota que recebe uma string na var name
def hello(name):
        return f"<h1>Hello, {name}!</h1>" #retorna a execuçaõ da função usando o placeholder da variável name
# ou seja, é uma rota dinâmica


