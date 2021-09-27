
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,current_user
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


class Role(db.Model):
    __tablename__ ='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    


    def __repr__(self):
        return f'User {self.name}'





class Quote(db.Model):
    __tablename__= 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    category = db.Column(db.String)
    date = db.Column(db.DateTime,default=datetime.utcnow)




    def save_quote(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_pitch(cls,id):
        pitches = Quote.query.filter_by(id=id).all()
        return pitches

    @classmethod
    def get_all_pitches(cls):
        pitches = Quote.query.order_by('-id').all()
        return pitches


    def __repr__(self):
        return f'Quote {self.pitch_title}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment_content = db.Column(db.String())
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(quote_id=id).all()
        return comments

    @classmethod
    def get_all_comments(cls,id):
        comments = Comment.query.order_by('id').all()
        return comments



class Like (db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer,primary_key=True)
    like = db.Column(db.Integer,default=1)
    


    def save_likes(self):
        db.session.add(self)
        db.session.commit()

    def add_likes(cls,id):
        like_pitch = Like(user = current_user, pitch_id=id)
        like_pitch.save_likes()

    @classmethod
    def get_likes(cls,id):
        like = Like.query.filter_by(quote_id=id).all()
        return like


    @classmethod
    def get_all_likes(cls,quote_id):
        likes = Like.query.order_by('-id').all()
        return likes


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'



class Dislike (db.Model):
    __tablename__ = 'dislikes'

    id = db.Column(db.Integer,primary_key=True)
    dislike = db.Column(db.Integer,default=1)


    def save_dislikes(self):
        db.session.add(self)
        db.session.commit()

    def add_dislikes(cls,id):
        dislike_pitch = Dislike(user = current_user, pitch_id=id)
        dislike_pitch.save_dislikes()

    @classmethod
    def get_dislikes(cls,id):
        dislike = Dislike.query.filter_by(quote_id=id).all()
        return dislike


    @classmethod
    def get_all_dislikes(cls,quote_id):
        dislikes = Dislike.query.order_by('-id').all()
        return dislikes


    def __repr__(self):
        return f'{self.user_id}:{self.quote_id}'        