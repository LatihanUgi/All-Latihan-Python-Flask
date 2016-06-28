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
		
andi = Tabungan("1234",0)
andi.tambahSaldo(5000)
print("Saldo Andi : " + str(andi.CekSaldo()))
budi = Tabungan("4321",15000)
budi.tambahSaldo(15000)
print("Saldo Budi : " + str(budi.CekSaldo()))
