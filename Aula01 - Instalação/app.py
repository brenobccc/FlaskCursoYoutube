from flask import Flask#importação

#coloca instancia de flask em uma variavel
app = Flask(__name__)

#criação de rotas
#decorator ou função
#decorator

@app.route("/")
def index():
	return "Index"

@app.route("/teste")
def teste():
	return "Teste"

if __name__ == '__main__':
	app.run()	#executar