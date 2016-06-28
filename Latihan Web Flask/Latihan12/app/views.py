from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ugi Ispoyo Widodo'}  # fake user
    return '''
<html>
  <head>
    <title>Website Pertamaku</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''