def cetak():
	print("Max: "+str(max))
	print("Min: "+str(min))
	print("Rata Rata: "+str(data/hitung))

a = 0
min = 100000
max = 0
data = 0
hitung = 0
while(a != -1):
	a = int (input("Masukan Bilangan: "))
	if (a==-1):
		break
	else:
		if(a>max):
			max = a
		if(a<min):
			min = a
		hitung = hitung +1
		data = data + a
cetak()

#latihan prosedeural