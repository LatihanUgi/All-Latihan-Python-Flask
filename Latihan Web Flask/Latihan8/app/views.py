from flask import render_template
from app import app
import MySQLdb
import demjson

@app.route('/')
@app.route('/index')
def index():
	list = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")
	cursor = db.cursor()
	sql = "select * from tb_admin"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			id = row[0]
			nama = row[1]
			list.append({'id':id,'nama':nama})
	except:
		print "Error: Unable to fecth data!"
	db.close()
	return render_template("index.html",list = list)
@app.route('/')
@app.route('/json')
def json():
	list = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")
	cursor = db.cursor()
	sql = "select * from tb_admin"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			id = row[0]
			nama = row[1]
			list.append({'id':id,'nama':nama})
		json = demjson.encode(list)
	except:
		print "Error: Unable to fecth data!"
	db.close()
	return render_template("json.html",data = json)
@app.route('/')
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/')
@app.route('/profile')
def profile():
	return render_template("profile.html")