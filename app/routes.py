from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, EditProfileForm, PostForm
from app.models import User, Post
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime


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

# Note: login_required makes the view accessible iff the user is logged in.
#       current_user is a flask global for the user currently logged in

#@app.route('/')
#@app.route('/index')
#@login_required
#def index():
#  return render_template('index.html',
#                         title = 'the sickest title',
#                         purchases = recent_purchases)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)

    # see config.py for setting POSTS_PER_PAGE
    posts = current_user.get_posts().paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None

    return render_template('index.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():

# current_user is from flask-login. It can be a user object from the database,
# or a special anonymous user object if the user did not log in yet.
  if current_user.is_authenticated:
      return redirect(url_for('index'))

  form = LoginForm()

  if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()

      if user is None or not user.check_password(form.password.data):
          flash('Invalid username or password')
          return redirect(url_for('login'))

      login_user(user, remember=form.remember_me.data)

      next_page = request.args.get('next')
      if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('index')

      return redirect(next_page)

  return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Goal: not suck'},
        {'author': user, 'body': 'Goal: get the moneyz!'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
      current_user.last_seen = datetime.utcnow()
      db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():

    form = EditProfileForm(current_user)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template('edit_profile.html', title='Edit Profile', form=form)
