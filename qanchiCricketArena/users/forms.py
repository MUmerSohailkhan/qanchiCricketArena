from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from qanchiCricketArena.models import user


class requestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Request Reset Form')

    def validate_email(self,email):
        user1 = user.query.filter_by(email=email.data).first()
        if user1 is None:
            raise ValidationError('There is no account associated with this email.You must register first')


class resetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirmPassword = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Reset Password')

class  registrationForm(FlaskForm):
    username=StringField('User Name',validators=[DataRequired(),Length(min=3,max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6)])
    confirmPassword=PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Submit')

    def validate_username(self,username):
        user1 = user.query.filter_by(username=username.data).first()
        if user1:
            raise ValidationError('This user name already exist please choose otherone')
    def validate_email(self,email):
        user1 = user.query.filter_by(email=email.data).first()
        if user1:
            raise ValidationError('This email already exist please choose otherone')

class  loginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    rememberMe=BooleanField('Remember Me')
    submit=SubmitField('Login')

class  updateAccountForm(FlaskForm):
    username=StringField('User Name',validators=[DataRequired(),Length(min=3,max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data!=current_user.username:
            user1 = user.query.filter_by(username=username.data).first()
            if user1:
                raise ValidationError('This user name already exist please choose otherone')
    def validate_email(self,email):
        if email.data!=current_user.email:
            user1 = user.query.filter_by(email=email.data).first()
            if user1:
                raise ValidationError('This email already exist please choose otherone')
