from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[required()])
    review = TextAreaField('Movie review')
    submit =SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [required()])
    submit = SubmitField('Submit')


