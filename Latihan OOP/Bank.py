class Tabungan:
	def __init__(self,no_rek,saldo):
		self.no = no_rek
		self.balance = saldo
	def tambahSaldo(self,saldo):
		self.balance = self.balance+saldo
	def cekSaldo(self):
		return self.balance
	def kurangSaldo(self,saldo):
		self.balance = self.balance - saldo
class Customer:
	def __init__(self,nama,kota):
		self.nama = nama
		self.kota = kota
		self.tabungan = []
	def tambahTabungan(self,tabungan):
		self.tabungan.append(tabungan)
	def cetakTabungan(self):
		for i in self.tabungan:
			print (i.no+" : "+str(i.cekSaldo()))
			
andi = Customer("Andi","Bandung")
andi.tambahTabungan(Tabungan("123",0))
andi.tambahTabungan(Tabungan("321",1000))
andi.cetakTabungan()