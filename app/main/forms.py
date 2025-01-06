from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    email_choice = StringField('Qual é o seu email (Envio de notificação do novo usuário)?',  validators=[DataRequired(), Email(message="Email com formato incorreto")])
    submit = SubmitField('Submit')