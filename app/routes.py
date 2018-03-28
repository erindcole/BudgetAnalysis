from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

# mock some objects
user1 = {'username': 'metal man'}
user2 = {'username': 'metal woman'}

# good old mock html template
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
'''.format(user1['username'])

recent_purchases = [{
                      'user': user1,
                      'description': "shit you didn't need",
                      'cost': 9999999999.99
                    },
                    {
                      'user': user2,
                      'description': "that good good",
                      'cost': "a billion dollars"
                    }]

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html',
                         title = 'the sickest title',
                         user=user1, purchases = recent_purchases)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      flash('Login requested for user {}, remember_me={}'.format(
          form.username.data, form.remember_me.data))
      return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)
