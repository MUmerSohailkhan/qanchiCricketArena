from flask_wtf import FlaskForm
from wtforms import fields,validators


class bookingForm(FlaskForm):
    dateBooked = fields.DateField('dateBooked', format='%Y-%m-%d',validators=[validators.DataRequired()])
    timeBooked = fields.TimeField('timeBooked', format='%H:%M',validators=[validators.DataRequired()])
    submit=fields.SubmitField('Submit Booking')

