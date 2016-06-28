
import MySQLdb

db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython")

cursor = db.cursor()

sql = "select * from tb_admin"
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		id = row[0]
		nama = row[1]
		print "id=%s,nama=%s" % \
			(id,nama,)
except:
	print "Error: Unable to fecth data!"
db.close()