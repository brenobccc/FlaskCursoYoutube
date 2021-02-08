#aula 04 - Contrução de URL
#redirecionamento

from flask import Flask,redirect,url_for#:para construir URLS

app = Flask(__name__)


@app.route("/admin")
def admin():
	return "<h1>Admin</h1>"
#code

@app.route("/guest/<name>")
def guest(name):
	return '<p>Olá guest <b>%s</b></p>' % name
if __name__ == '__main__':
	app.run(debug=True)