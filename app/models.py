from app import db

class Notes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200))
    filename=db.Column(db.String(200), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(100))
    email=db.Column(db.String(100), nullable=False,unique=True)
    password_hashed=db.Column(db.String(300), nullable=False)