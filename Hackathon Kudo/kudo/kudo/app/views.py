from app import app
import psycopg2

@app.route('/')
@app.route('/index') #route ke login, dengan method get dan post
def index(): #panggil procedure login
	stat = True
	status = False
	conn = psycopg2.connect(database='postgres', user='postgres', password='031191', host='localhost', port='5432')
	cur = conn.cursor()
	cur.execute("SELECT * from data.store")
	rows = cur.fetchall()
	data = "[" #"{\"result\":["
	for row in rows:
		if(stat == False):
			data = data + ","
		status = True
		data = data + "{\"id_item\":\""+str(row[0])+"\",\"nama\":\""+str(row[1])+"\",\"pts\":\""+str(row[2])+"\",\"deskripsi\":\""+str(row[3])+"\",\"foto\":\""+str(row[4])+"\",\"stock\":\""+str(row[5])+"\"}"
		stat = False
	if(status==False):
		data = data + "{\"id_item\":\"0\",\"nama\":\"Kosong\",\"pts\":\"0\",\"deskripsi\":\"kosong\",\"foto\":\"kosong\",\"stock\":\"0\"}"
	#data = data + "]}"
	data = data + "]"
	conn.close()
	return data