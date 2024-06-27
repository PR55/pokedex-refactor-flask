from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    happiness= IntegerField("Happiness", validators=[DataRequired()])
    price=IntegerField("Price", validators=[DataRequired()])
    



class CreatePokemonForm(FlaskForm):
    number= IntegerField("Number", validators=[DataRequired()])
    attack=StringField("Attack", validators=[DataRequired()])
    defense=StringField("Defense", validators=[DataRequired()])
    ## or FileField
    imageUrl=StringField("Image URL")
    name= StringField("Name", validators =[DataRequired()])
    type= SelectField("Type")
    move1= StringField("Move 1")
    move2= StringField("Move 2")