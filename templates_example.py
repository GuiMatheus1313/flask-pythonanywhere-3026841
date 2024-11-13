# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template, session, url_for, redirect, flash
from datetime import datetime

#Parte SQL
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


from flask_moment import Moment
#Parte do WTF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

#parte SQL
app.config['SQLALCHEMY_DATA_URI'] = \'sqlite:///' + os.path.join(basedir, 'data.sqlite)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Parte do WTF
app.config['SECRET_KEY'] = 'chave forte'

moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    sobreNome = StringField('Qual teu sobrenome?', validators = [DataRequired()])
    inst = StringField('Informe a sua Insituição de ensino:', validators = [DataRequired()])
    disciplina = SelectField('Informe a sua disciplina', choices=[('Desenvolvimento Web: Servidor', 'DWEBS'), ('Gestão de TI', 'GSTI'), ('Projeto de Extensão 4', 'EX4')])
    submit = SubmitField('Submit')

#Essa rota está para uso do forms
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = NameForm()
    if form.validate_on_submit():
        session['navegador'] = request.headers.get('User-Agent')
        session['Ip_remoto'] = request.headers.get('X-Forwarded-For')
        session['host_name'] = request.headers.get('Host')
        session['name'] = form.name.data
        session['sobreNome'] = form.sobreNome.data
        session['inst'] = form.inst.data
        session['disciplina'] = form.disciplina.data
        return redirect(url_for('hello_world'))
    return render_template('formularioTeste.html', form = form, name = session.get('name'), sobreNome = session.get('sobreNome'), inst = session.get('inst'), disciplina = session.get('disciplina'),
    browser = session.get('navegador'), ip_remoto = session.get('Ip_remoto'), host_name = session.get('host_name'), current_time = datetime.utcnow())
