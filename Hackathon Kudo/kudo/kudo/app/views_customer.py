from app import app
import psycopg2

@app.route('/rekomendasistoreid')
def rekomendasistoreid():
	data = ""
	conn = psycopg2.connect(database='postgres', user='postgres', password='031191', host='localhost', port='5432')
	cur = conn.cursor()
	cur.execute("SELECT * from data.store where (stat_retweet='Banyak' OR stat_follower='Banyak') OR (stat_retweet='Banyak' OR stat_fblike='Banyak')")
	rows = cur.fetchall()
	i = 0
	for row in rows:
		data = data + str(row[0])+"#"
		i = i + 1
	conn.close()
	return data

@app.route('/collaborative/<idp>')
def collaborative(idp):
	data = " "
	arr = {}
	conn = psycopg2.connect(database='postgres', user='postgres', password='031191', host='localhost', port='5432')
	cur = conn.cursor()
	cur.execute("SELECT id_user from data.transaksi where id_item = '"+str(idp)+"'")
	rows = cur.fetchall()
	for row in rows:
		cur.execute("SELECT id_item from data.transaksi where id_user = '"+str(row[0])+"'")
		rows_item = cur.fetchall()
		for row_item in rows_item:
			if(arr.get(str(row_item[0]))==None):
				arr.update({str(row_item[0]):1})
			else:
				nilai = arr.get(str(row_item[0])) + 1
				arr.update({str(row_item[0]):nilai})
	data = "<h1>REKOMENDASI PRODUK</h1>"
	data = data + "<p>Berikut merupakan rekomendasi produk (item to item collaborative filtering)</p>"
	for key in arr:
		cur.execute("SELECT B.id_item,B.judul,B.harga from data.item B where B.id_item='"+key+"'")
		rowsd = cur.fetchall()
		i = 0
		for rowd in rowsd:
			data = data + "Nama Item : " + str(rowd[1])+", "
			data = data + "harga : " + str(rowd[2])+", </br>"
			i = i + 1
	data = data + "</br><p>Berikut merupakan rekomendasi produk based on transparancy Merchant</p>"
	transparantstore = rekomendasistoreid().split("#")
	for tr in transparantstore:
		for key in arr:
			cur.execute("SELECT B.id_item,B.judul,B.harga,A.id_store,A.nama from data.item B,data.store A where A.id_store=B.id_store AND B.id_item='"+key+"' AND B.id_store='"+tr+"'")
			rowsd = cur.fetchall()
			i = 0
			for rowd in rowsd:
				#data = data + "ID Item : " + str(rowd[0])+", "
				data = data + "Nama Item : " + str(rowd[1])+", "
				data = data + "harga : " + str(rowd[2])+", "
				data = data + "ID Merchant : " + str(rowd[3])+"', "
				data = data + "Nama Merchant : " + str(rowd[4])+"'</br>"
				i = i + 1
	conn.close()
	return data