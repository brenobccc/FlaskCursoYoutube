from flask import Flask 

app = Flask(__name__)

#configurando outras informações
@app.route("/")
def index():
	#d = 3/0 #erro, o debug mostra detalhado
	return "index"


@app.route("/teste")
def teste():
	return "<p>Testando 1</p>"

def teste2():
	return "<p>Testando 2</p>"
				#regra    #endpoint(nome da funcao)
#app.add_url_rule("/teste","teste",teste)
app.add_url_rule("/teste-2","teste2",teste2)

if __name__ == "__main__":        #view function
	app.run(debug=True, port="3000")