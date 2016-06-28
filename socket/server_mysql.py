#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import MySQLdb

def lihatData():
	db = MySQLdb.connect('127.0.0.1','root','','latihanwebpython')

	cursor = db.cursor()
	hasil = "Data : \n"

	sql = "SELECT * FROM tb_admin"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			id = row[0]
			nama = row[1]
			#print "id = %s | nama = %s" % \
			#	(id, nama, )
			hasil = hasil + "\nid = "+id+"\nnama = "+nama
			
			#print 'berhasil koneksi'
			
			#print 'tambah data dari server dhana'

	except:
		print "Error: Unable to fecth data"
	return hasil
	db.close

s = socket.socket()         # Create a socket object
host = '192.168.43.141' # Get local machine name
port = 2222                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Server Ugi - Got connection from', addr
	data = c.recv(1024)
	if(data == '1'):
		c.send('Tambah data berhasil dari server ugi ganteng banget')
		print 'tambah data dari server ugi'
	elif(data == '2'):
		c.send(lihatData())
		#c.send('Lihat Data Berhasil dari server dhana keren')
		#print 'lihat data dari server dhana'
	c.close()                # Close the connection
	break