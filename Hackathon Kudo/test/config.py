from os import path

# App details
app.config['SECRET_KEY'] = '33218295e6debb4296144c45dc381eec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
	'facebook': {
		'id': '278380555842361',
	   'secret': '33218295e6debb4296144c45dc381eec'
	}
}