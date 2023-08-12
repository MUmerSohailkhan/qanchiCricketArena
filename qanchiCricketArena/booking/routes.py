from flask import render_template,request,Blueprint,redirect,url_for
from qanchiCricketArena.models import booking
from qanchiCricketArena import db
bookingB=Blueprint('bookingB',__name__)
from qanchiCricketArena.booking.forms import bookingForm
from flask_login import current_user,login_required





@login_required
@bookingB.route("/booking",methods=['Post','GET'])
def bookingPageFunc():
    form=bookingForm()
    if form.validate_on_submit():
        print(form.timeBooked.data)
        print(form.dateBooked.data)
        print(current_user)
        booking1=booking(timeBooked=form.timeBooked.data,dateBooked=form.dateBooked.data,author=current_user)
        db.session.add(booking1)
        db.session.commit()
        return redirect(url_for('mainB.homePageFunc'))
    return render_template('bookingPage.html',legend='New Booking',form=form)