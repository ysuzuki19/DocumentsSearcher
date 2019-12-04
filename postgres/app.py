from flask import Flask, render_template, request
from hamlish_jinja import HamlishExtension
from werkzeug import ImmutableDict
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/PostgreSQL12'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
	return render_template('form.html')

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/confirm', methods=['POST', 'GET'])
def confirm():
	if request.method == 'POST':
		result = request.form
	return render_template('confirm.html', result=result)

if __name__ == '__main__':
	app.run(host='localhost', debug=True)

