from datetime import datetime
from flask import current_app
from qanchiCricketArena import db,login_manager
from flask_login import UserMixin
from itsdangerous import Serializer




@login_manager.user_loader
def loadUser(user_id):
    return user.query.get(int(user_id))


class user(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(20),unique=True,nullable=False)
    imageFile=db.Column(db.String(20),nullable=False,default='defImage1.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('post',backref='author',lazy=True)
    bookings=db.relationship('booking',backref='author',lazy=True)


    def get_reset_token(self,expiresSec=1800):
        s=Serializer(current_app.config['SECRET_KEY'],expiresSec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id=s.loads(token)['user_id']
        except:
            return None
        return user.query.get(user_id)
    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.imageFile}')"



class post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    datePosted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    userId=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f"post('{self.title}','{self.datePosted}')"



class booking(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    bookingTime=db.Column(db.DateTime,nullable=False,default=datetime.now)
    timeBooked=db.Column(db.Time,nullable=False)
    dateBooked=db.Column(db.Date,nullable=False)
    userId=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

