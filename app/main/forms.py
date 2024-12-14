from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    email_choice = BooleanField('Deseja enviar para o email do administrador?')
    submit = SubmitField('Submit')