from app import app


user = {'username': 'Mark'}
page = '''
<html>
  <head>
    <title> This is the Title </title>
    <p> paragraph in the header? </p>
  <head>

  <body>
    <h1>This is the header in the body: Hello {} !</h1>
    <p>This is a paragraph in the body</p>
  </body>
</html>
'''.format(user['username'])

@app.route('/')
@app.route('/index')
def index():
  return page
