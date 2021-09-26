
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    passcode = db.Column(db.String(255))
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.passcode = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.passcode, password)
    def __repr__(self):
        return f'User {self.username}'
#api endpoint class
class Quote_Body:
    _data = []
    def __init__(self, quote, author, permalink):
        self.quote = quote
        self.author = author
        self.permalink = permalink