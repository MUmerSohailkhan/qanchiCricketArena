import secrets,os
from PIL import Image
from qanchiCricketArena import mail
from flask import url_for,current_app
from flask_mail import Message

def sendResetEmail(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request',sender='noreply@demo.com'
                ,recipients=[user.email])
    msg.body=f'''To reset your password ,visit the following link
    {url_for('resetTokenPageFunc',token=token, _external=True)}
    If you did not make this report simply ignore this email'''
    mail.send(msg)


def savePicture(formPicture):
    randomHex=secrets.token_hex(8)
    fName,fExt=os.path.splitext(formPicture.filename)#splitting pic file name
    pictureFullName=randomHex+fExt
    picturePath=os.path.join(current_app.root_path,'static/profilePics',pictureFullName)

    #resizing and saving picture

    outputSize=(125,125)
    i=Image.open(formPicture)
    i.thumbnail(outputSize)
    i.save(picturePath)

    return pictureFullName