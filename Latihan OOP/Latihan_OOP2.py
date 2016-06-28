class Tabungan:
	def __init__(self,no_rek,saldo):
		self.no_rek = no_rek
		self.saldo = saldo
		
	def tambahSaldo(self,saldo):
		self.saldo = self.saldo + saldo
	
	def CekSaldo(self):
		return self.saldo
		
	def kurangSaldo(self,saldo):
		self.saldo = self.saldo - saldo
		
class Customer:
	Tabungan[]
	def __init__(self,nama,kota):
		self.nama = nama
		self.kota = kota
	
	