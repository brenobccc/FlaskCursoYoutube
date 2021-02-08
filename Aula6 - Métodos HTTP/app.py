from flask import Flask, request
from json import dumps
					
app = Flask(__name__, static_folder='public')

#@app.route('/add',methods=["POST"])
@app.route('/add',methods=["GET","POST"]) 
def add():
	if request.method == "POST":#request.method: controla requisições
		#return "OKK POST result: %s." % request.form['nome']
		return dumps(request.form) 
	return "OKK GET"
if __name__ == '__main__':
	app.run(debug=True)