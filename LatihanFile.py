file = open("data.txt","r+") #untuk menulis
str = file.readlines();
print (str)
for i in str:
	print(i)
file.close()

#file = open("data.txt","a") #untuk menulis baru
#print ("Nama : ", file.name)
#s = input("Masukan Nama Anda : ")
#file.write(s)