
import socket 

def sendMessage(cmd):
	s = socket.socket()
	host = raw_input('Masukan IP : ')
	port = int(raw_input('Masukan Port : '))
	
	s.connect((host,port))
	s.send(cmd)
	data = s.recv(1204)
	print data
	
	s.close

print '1. Tambah Data'
print '2. Lihat Data'
pil = raw_input('pilihan Anda : ')
if(pil=='1'):
	sendMessage('1')
elif(pil=='2'):
	sendMessage('2')