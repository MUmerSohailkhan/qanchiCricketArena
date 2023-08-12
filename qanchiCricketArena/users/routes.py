from flask import Blueprint
from flask import render_template,url_for,flash,redirect,request,abort
from qanchiCricketArena.models import user
from qanchiCricketArena.users.forms import registrationForm,loginForm,updateAccountForm,requestResetForm,resetPasswordForm
from qanchiCricketArena import db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required
from qanchiCricketArena.users.utils import savePicture,sendResetEmail

usersB=Blueprint('usersB',__name__)





#routes

@usersB.route("/registration",methods=['POST','GET'])
def registrationPageFunc():
    if current_user.is_authenticated:
        return redirect(url_for('mainB.homePageFunc'))
    form=registrationForm()
    if form.validate_on_submit():
        hashedPassword=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user1=user(username=form.username.data,email=form.email.data,password=hashedPassword)
        db.session.add(user1)
        db.session.commit()
        flash(f"Your account has been created !You are now able to login",'success')
        return redirect(url_for('usersB.loginPageFunc'))
    return render_template('registration.html',form=form)




@usersB.route("/login",methods=['POST','GET'])
def loginPageFunc():
    if current_user.is_authenticated:
        return redirect(url_for('mainB.homePageFunc'))
    form=loginForm()
    if form.validate_on_submit():
        user1=user.query.filter_by(email=form.email.data).first()
        if user1 and bcrypt.check_password_hash(user1.password,form.password.data):
            login_user(user1,remember=form.rememberMe.data)
            nextPage=request.args.get('next')
            return redirect(url_for('usersB.accountPageFunc')) if nextPage else redirect(url_for('mainB.homePageFunc'))
        else:
            flash(f"Login Unsuccessful, please try again with valid email and password",'danger')
    return render_template('login.html',title='Login',form=form)


@usersB.route("/logout")
def logoutPageFunc():
    logout_user()
    return render_template('logout.html',title='Logout')





@usersB.route("/account",methods=['POST','GET'])
@login_required
def accountPageFunc():
    form=updateAccountForm()
    if form.validate_on_submit():
        if form.picture:
            pictureFile=savePicture(form.picture.data)
            current_user.imageFile=pictureFile
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('your account has been updated','success')
        return redirect(url_for('usersB.accountPageFunc'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    imageFile=url_for('static',filename=f'profilePics/{current_user.imageFile}')
    return render_template('account.html',title='Account',imageFile=imageFile,form=form)




@usersB.route("/resetPassword",methods=['POST','GET'])
def resetRequestPageFunc():
    if current_user.is_authenticated:
        return redirect(url_for('main.homePageFunc'))
    form=requestResetForm()
    if form.validate_on_submit():
        user1=user.query.filter_by(email=form.email.data).first()
        sendResetEmail(user1)
        flash('An Email has been sent with instruction to reset your password')
        return redirect(url_for('users.loginPageFunc'))
    return render_template ('resetRequest.html',form=form,title='Reset Password')



@usersB.route("/resetPassword/<token>",methods=['POST','GET'])
def resetTokenPageFunc(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.homePageFunc'))
    user1=user.verify_reset_token(token)
    if user1 is None:
        flash('This is invalid or expires token')
        return redirect(url_for('users.resetRequestPageFunc'))
    form=resetPasswordForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user1.password=hashedPassword
        db.session.commit()
        flash(f"Your password has been updated !You are now able to login", 'success')
        return redirect(url_for('users.loginPageFunc'))
    return render_template ('resetToken.html',form=form,title='Reset Password')

