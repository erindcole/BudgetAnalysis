from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from os import path

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        # get unique usernames
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        # get a unique email
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired()])
  about_me = TextAreaField('About Me', validators = [Length(min=0, max=140)])
  submit = SubmitField('Submit')

  def __init__(self, original_username, *args, **kwargs):
      super(EditProfileForm, self).__init__(*args, **kwargs)
      self.original_username = original_username

  def validate_username(self, username):
      if username.data != self.original_username:
          user = User.query.filter_by(username=self.username.data).first()
          if user is not None:
              raise ValidationError('That name is taken. Please use a different username.')

class PostForm(FlaskForm):
   title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=64)])
   post = TextAreaField('Body', validators=[DataRequired(), Length(min=1, max=140)])
   submit = SubmitField('Submit')

class ExploreForm(FlaskForm):
  """
   TODO: need to have a better way for users to point to their data
  """
  data_path = StringField("Path to Data", validators = [DataRequired()])
  submit = SubmitField('Submit')

  def validate_data_path(self, path_data):

    if not path.exists(path_data.data):
      raise ValidationError('Unable to find data given location.')

    if not path.isfile(path_data.data) or not path_data.data.lower().endswith('.csv'):
      raise ValidationError('File must be a CSV file.')
