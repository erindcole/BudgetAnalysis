from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    purchases = db.relationship('Purchase', backref='user', lazy=True)


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))
    date = db.Column(db.Date)
    amount = db.Column(db.Numeric(19, 4))
    balance = db.Column(db.Numeric(19, 4))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Purchase {}>'.format(self.username)
