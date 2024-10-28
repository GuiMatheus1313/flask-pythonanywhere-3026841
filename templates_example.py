# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template, session, url_for, redirect, flash
from datetime import datetime


from flask_moment import Moment
#Parte do WTF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


#Parte do WTF
app.config['SECRET_KEY'] = 'chave forte'

moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    submit = SubmitField('Submit')

#Essa rota está para uso do forms
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Mudando nome!')
        session['name'] = form.name.data
        return redirect(url_for('hello_world'))
    return render_template('formularioTeste.html', form = form, name = session.get('name'))
"""
@app.route('/')
def hello_world():
    name = "eu estou usando o JINJA2!";
    return render_template('template-base.html', current_time = datetime.utcnow());
"""
@app.route('/user/<name>')
def hello_pront(name):
    name2 = name
    return render_template('user.html', name = name, pront = 'PT3026841', ins = 'IFSP' , current_time = datetime.utcnow())


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', current_time = datetime.utcnow()), 404;

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return render_template('contextorequisicao.html', name = 'Guilherme', navegador = navegador, IP_cliente = Ip_remoto, host_name = host_name);