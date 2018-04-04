# This branch deals with creating a restful flask app.

##Dependencies:
- flask
export FLASK_APP=microblog.py

- flask-wtf
- flask-sqlalchemy
- flask-migrate

- flask-login
- flask-bootstrap

##Starting the Server
export FLASK_APP=microblog.py
$flask run

##Track change to the database
flask db migrate -m "posts table"

##Applying the change to the database
flask db upgrade
