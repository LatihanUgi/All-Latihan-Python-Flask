from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Ugi Ispoyo Widodo'}  # fake user
	return render_template('index.html',
							title='Home1',
							user=user)