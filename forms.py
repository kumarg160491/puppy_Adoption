from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class ADDForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('ADD Puppy')


class DelForm(FlaskForm):

    id = IntegerField('ID number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')