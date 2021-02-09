from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'#Conexão com o banco de dados

db = SQLAlchemy(app)
class Estudante(db.Model):
	id = db.Column('id',db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(150))
	idade = db.Column(db.Integer)
	def __init__(self,nome,idade):
		self.nome = nome
		self.idade = idade 

@app.route('/')
def index():
	estudantes = Estudante.query.all()
	return render_template('index.html',estudantes=estudantes)

@app.route('/add', methods=['GET','POST'])
def add():
	if request.method == 'POST':
		estudante = Estudante(request.form['nome'], request.form['idade'])
		db.session.add(estudante)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('add.html')
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)