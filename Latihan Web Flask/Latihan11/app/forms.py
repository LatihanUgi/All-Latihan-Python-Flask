from flask.ext.wtf import Form #library wtf -> ambil Form
from wtforms import StringField, BooleanField, PasswordField, FileField  #stringfield untuk input string, booleanfield untuk input boolean
from wtforms.validators import DataRequired #ini validator, untuk menjalankan validasi tiap data yg di submit

class Input(Form): #class SignUp untuk signup
	nama = StringField('Nama', validators = [DataRequired()])
	file = FileField()
class Produk(Form): #class SignUp untuk signup
	nama = StringField('Nama', validators = [DataRequired()])
	harga = StringField('Harga', validators = [DataRequired()])
	stok = StringField('Stok', validators = [DataRequired()])