from flask import Flask 

app = Flask(__name__)

#code
#url_dinamicas = caso a gente queira obter uma informação da url
#post, titulo da url, mostrar o conteudo
@app.route('/hello/')
@app.route("/hello/<nome>")
def hello(nome=""):
	return "<h1>Hello {}</h1>".format(nome)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
	if postID >= 0:
		return "blog info {}".format(postID)
	else:
		return "blog todo"

if __name__ == "__main__":
	app.run(debug=True) 