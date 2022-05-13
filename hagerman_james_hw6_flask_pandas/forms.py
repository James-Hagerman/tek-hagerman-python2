from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    age = IntegerField('Age of Puppy: ')
    breed = StringField('Breed of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of owner: ')
    pup_id = IntegerField("Id of Puppy: ")
    submit = SubmitField('Add Owner')

# class AddPupsToys(FlaskForm):

#     pup_id = IntegerField('Id of Puppy: ')
#     submit = SubmitField('Add Toy')