from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html', judul='Home')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', data = 'Tidak Ditemukan')
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html', data = 'Maintenance')
	
if __name__ == '__main__':
	app.run(debug = True)