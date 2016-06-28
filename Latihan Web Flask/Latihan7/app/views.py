from flask import render_template
from app import app
import MySQLdb
import demjson

@app.route('/')
@app.route('/index')
def index():
	listData = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")
	cursor = db.cursor()
	try:
		cursor.execute("select * from tb_admin")
		results = cursor.fetchall()
		for row in results:
			id = str(row[0])
			nama = row[1]
			listData.append
			(
				{
					'id':id,
					'nama':nama
				}
			)
	except:
		print "Error: Unable to fecth data!"
	db.close()
	return render_template("index.html",title='home',
							posts=listData)

@app.route('/')
@app.route('/json')
def json():
	listData = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")
	cursor = db.cursor()
	try:
		cursor.execute("select * from tb_admin")
		results = cursor.fetchall()
		for row in results:
			id = str(row[0])
			nama = row[1]
			listData.append
			(
				{
					'id':id,
					'nama':nama
				}
			)
		json = demjson.encode(listData)
	except:
		print "Error: Unable to fecth data!"
	db.close()
	return render_template("json.html",
							data=json)

@app.route('/')
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/')
@app.route('/profile')
def profile():
	return render_template("profile.html")