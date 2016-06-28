#!/usr/bin/python

import socket

s = socket.socket() #open socket
host = '192.168.43.141' #ambil hostname
port = 2222	#setting port ke variable port
s.bind((host, port))	#koneksi dengan hostname

s.listen(5) #tunggu selama 5 ms
while True:
	c, addr = s.accept()
	print 'Server Ugi - Got connection Form', addr
	data = c.recv(1024)
	if(data=='1'):
		c.send('Tambah Data Berhasil dari server ugi')
		print'tambah data dari server ugi'
	elif(data=='2'):
		c.send('Lihat Data Berhasil server ugi')
		print'lihat data dari server ugi'
	c.close()
	break