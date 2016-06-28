from flask.ext.wtf import Form #library wtf -> ambil Form
from wtforms import StringField, BooleanField, HiddenField,FileField,SelectField   #stringfield untuk input string, booleanfield untuk input boolean
from wtforms.validators import DataRequired #ini validator, untuk menjalankan validasi tiap data yg di submit

class Input(Form): #class SignUp untuk signup
	nama = StringField('Nama', validators = [DataRequired()])
	file = FileField()
class Login(Form): #class SignUp untuk signup
	username = StringField('Username', validators = [DataRequired()])