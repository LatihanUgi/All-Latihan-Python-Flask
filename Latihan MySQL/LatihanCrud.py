import MySQLdb

def lihatAdmin():
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")

	cursor = db.cursor()

	sql = "select * from tb_admin"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print 'Data Admin : '
		for row in results:
			nama = row[1]
			roles = row[3]
			print "Username = %s, Roles = %s" % \
				(nama,roles,)
	except:
		print "Error: Unable to fecth data!"
	db.close()
	
def tambahAdmin():
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")

	cursor = db.cursor()
	try:       
		input1 = raw_input('Input user :')
		input2 = raw_input('Input password :')
		input3 = raw_input('Input roles :')
		sql = "INSERT INTO tb_admin(user,pass,roles) VALUES('"+input1+"','"+input2+"','"+input3+"')"
		cursor.execute(sql)
		db.commit()
	except:
		print "Error: Unable to fecth data!"
	db.close()
	
def hapusAdmin():
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")

	cursor = db.cursor()
	try:       
		cursor.execute("select * from tb_admin")
		results = cursor.fetchall()
		print 'Data Admin'
		for row in results:
			id = row[0]
			nama = row[1]
			roles = row[3]
			print "ID = %s , Username = %s, Roles = %s" % \
				(id,nama,roles,)
		inputhapus = raw_input("Input ID Admin Yang Akan Di Hapus : ")
		sqlhapus = "DELETE FROM tb_admin WHERE id_admin = %s"
		cursor.execute(sqlhapus, inputhapus)
		db.commit()
	except:
		print "Error: Unable to fecth data!"
	db.close()
	
def ubahAdmin():
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")

	cursor = db.cursor()
	try:       
		cursor.execute("select * from tb_admin")
		results = cursor.fetchall()
		print 'Data Admin'
		for row in results:
			id = row[0]
			nama = row[1]
			roles = row[3]
			print "ID = %s , Username = %s, Roles = %s" % \
				(id,nama,roles,)
		inputubah = raw_input("Input ID ADMIN YANG MAU DI HAPUS : ")
		inputubah1 = raw_input("Input Nama : ")
		inputubah2 = raw_input("Input Password : ")
		inputubah3 = raw_input("Input Roles : ")
		sqlubah = "UPDATE tb_admin SET user = '"+inputubah1+"', pass= '"+inputubah2+"', roles= '"+inputubah3+"' WHERE id_admin=%s"
		cursor.execute(sqlubah, inputubah)
		db.commit()
	except:
		print "Error: Unable to fecth data!"
	db.close()

def halamanAdmin():
	print '1. Lihat Data Admin'
	print '2. Tambah Data Admin'
	print '3. Ubah Data Data'
	print '4. Hapus Data Data'
	pilih = raw_input('Masukan Pilihan Anda :')

	if (pilih =='1'):
		lihatAdmin()
	elif(pilih=='2'):
		tambahAdmin()
	elif(pilih=='3'):
		ubahAdmin()
	elif(pilih=='4'):
		hapusAdmin()

def loginAdmin(user,pswd):
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")
	cursor = db.cursor()
	try:       
		'''cursor.execute("select user from tb_admin where user = '"+user+"'")
		results1 = cursor.fetchone()
		if results1 != user:
			print 'Gagal Login!'
		else:'''
		cursor.execute("select * from tb_admin where user = '"+user+"'")
		results = cursor.fetchall()
		for row in results:
			if user == row[1]:
				if pswd == row[2]:
					halamanAdmin()
				else:
					print 'Gagal Login'
			else:
				print 'Gagal Login'
		db.commit()
	except:
		print "Error: Unable to fecth data!"
	db.close()

print 'Login : '
user = raw_input('Masukan Username : ')
pswd = raw_input('Masukan Password : ')
loginAdmin(user,pswd)
