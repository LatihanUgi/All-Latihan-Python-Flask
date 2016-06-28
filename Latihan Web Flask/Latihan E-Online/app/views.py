from flask import render_template, flash, redirect, request
from app import app
from .forms import Login #import data dari class LoginForms 
import MySQLdb

'''@app.route('/lihat') #route ke login, dengan method get dan post
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
			listData.append(
				{
					'id':id,
					'nama':nama
				}
			)
	except:
	   print "Error: unable to fecth data"
	db.close()
	return render_template("lihat.html",
							   title='Lihat Data',
							   posts=listData)'''
						   
@app.route('/loginadmin', methods=['GET', 'POST'])
def lgoinadmin():
	form = Login()
	if form.validate_on_submit():
		db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython" )
		cursor = db.cursor()
		try:
			nama = form.nama.data
			pswd = form.pswd.data
			cursor.execute("select * from e_admin where nama ='"+nama+"' and password = '"+pswd+"'")
			results = cursor.fetchone()
			if results:
				#return app.send_static_file('/halamanadmin.html')
				'''<script>alert('test')</script>'''
			else:
				return redirect('/loginadmin')
			'''for row in results:
				if nama == row[1]:
					if pswd == row[2]:
						return redirect('/halamanadmin')
					else:
						return redirect('/loginadmin')
				else:
					return redirect('/loginadmin')'''
			db.commit()
		except:
			print "Error: unable to fecth data"
	return render_template('loginadmin.html', 
                           title='Login Admin',
                           form=form)
						   	
'''@app.route('/hapus/<id>') #route ke login, dengan method get dan post
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
						   kirim=listData)'''