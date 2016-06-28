from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
DEBUG = True
SECRET_KEY = '33218295e6debb4296144c45dc381eec'

# Database details
SQLALCHEMY_DATABASE_URI = '{0}{1}'.format('sqlite:///', path.join(BASE_DIRECTORY, 'app.db'))