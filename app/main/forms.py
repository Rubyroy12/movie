from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import required

class ReviewForm(FlaskForm):
    title = StringField('Review_title', validators=[required()])
    review = TextAreaField('Review_review', validators=[required()])
    submit =SubmitField('Submit')


