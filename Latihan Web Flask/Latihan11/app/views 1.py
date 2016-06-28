from flask import render_template, flash, redirect, request, url_for, send_from_directory
from app import app
from .forms import Input #import data dari class LoginForms 
from werkzeug import secure_filename
#from .forms import Ubah
import MySQLdb
import os
import time
from random import randint

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/lihat') #route ke login, dengan method get dan post
def lihat(): #panggil procedure login
	listData = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
	cursor = db.cursor()
	try:
		cursor.execute("SELECT * FROM tb_admin") #menjalankan perintah sql
		results = cursor.fetchall()
		for row in results:
			id = str(row[0])
			nama = row[1]
			gambar = row[2]
			listData.append(
				{
					'id':id,
					'nama':nama,
					'gambar':gambar
				}
			)
	except:
	   print "Error: unable to fecth data"
	db.close()
	return render_template("lihat.html",
							   title='Lihat Data',
							   posts=listData)
						   
@app.route('/input', methods=['GET', 'POST'])
def input():
	form = Input()
	if form.validate_on_submit():
		#upload folder#
		file = request.files['file']
		if file and allowed_file(file.filename):
			uniq = (time.strftime("%d%m%Y%H%M%S")+str(randint(0,1000)))
			filename = secure_filename(file.filename)
			ekxtension = filename.rsplit('.',1)[1]
			filename = uniq + "."+ekxtension
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#end upload folder#
		db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
		cursor = db.cursor()
		try:
			nama = form.nama.data
			cursor.execute("insert into tb_admin(user,foto) values('"+nama+"','"+filename+"')") #menjalankan perintah sql
			results = cursor.fetchall()
			db.commit()
		except:
			print "Error: unable to fecth data"
		db.close()
		return redirect('/lihat')
	return render_template('input.html', 
                           title='Tambah Data',
                           form=form)
						   
@app.route('/hapus/<id>') #route ke login, dengan method get dan post
def hapus(id): #panggil procedure login
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
	cursor = db.cursor()
	try:
		cursor.execute("delete from tb_admin where id_admin="+id) #menjalankan perintah sql
		results = cursor.fetchall()
		db.commit()
	except:
	   print "Error: unable to fecth data"
	db.close()
	return redirect('/lihat')

@app.route('/ubah/<id>') #route ke login, dengan method get dan post
def ubah(id): #panggil procedure login
	listData = []
	#form1 = Ubah()
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
	cursor = db.cursor()
	try:
		cursor.execute("SELECT * FROM tb_admin where id_admin="+id) #menjalankan perintah sql
		results = cursor.fetchall()
		for row in results:
			id = str(row[0])
			nama = row[1]
			listData.append(
				{
					'id':id,
					'nama':nama
				}
			)
			#nama = form.requests.post(row[1])
			#nama = form.nama.data
	except:
	   print "Error: unable to fecth data"
	db.close()
	return render_template('ubah.html', 
                           title='Ubah Data',
						   kirim=listData)
				
@app.route('/ubahproses', methods=['GET', 'POST']) #route ke login, dengan method get dan post
def ubahproses(): #panggil procedure login
	listData = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
	cursor = db.cursor()
	try:
		nama = request.form['nama']
		id = request.form['id']
		sqlubah = "UPDATE tb_admin SET user = '"+nama+"' WHERE id_admin='"+id+"'"
		cursor.execute(sqlubah)
		db.commit()
	except:
	   print "Error: unable to fecth data"
	db.close()
	return redirect('/lihat')
	return render_template('ubah.html', 
                           title='Ubah Data',
						   kirim=listData)