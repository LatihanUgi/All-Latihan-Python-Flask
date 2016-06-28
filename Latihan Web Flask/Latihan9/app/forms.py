from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
	
class SignUp(Form):
	username = StringField('username', validators = [DataRequired()])
	email = StringField('email',validators = [DataRequired()])
	password = PasswordField('New Password',validators = [DataRequired()])
	accept_tos = BooleanField('accept_tos',default=False)