# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template, session, url_for, redirect, flash
from datetime import datetime

#Parte SQL
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

#Parte do Request e Thread e Mail
import os
import sys
from threading import Thread
from flask_mail import Mail, Message
import requests



from flask_moment import Moment
#Parte do WTF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

#parte SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Parte MAIL
app.config['API_KEY'] = os.environ.get('API_KEY')
app.config['API_URL'] = os.environ.get('API_URL')
app.config['API_FROM'] = os.environ.get('API_FROM')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
mail = Mail(app)

def send_simple_message(to, subject, newUser):
    #Registrando para o para o server log
    print('Enviando mensagem (POST)...', flush = True)
    print('URL: ' + str(app.config['API_URL']), flush = True)
    print('api: ' + str(app.config['API_KEY']), flush=True)
    print('from: ' + str(app.config['API_FROM']), flush=True)
    print('to: ' + str(to), flush=True)
    print('subject: ' + str(app.config['FLASKY_MAIL_SUBJECT_PREFIX']) + ' ' + subject, flush=True)
    print('text: ' + "Novo usuário cadastrado: " + newUser, flush=True)

    #Fazer a parte de http
    resposta = requests.post(app.config['API_URL'],
                            auth=("api", app.config['API_KEY']),
                            data={"from": app.config['API_FROM'],
                                "to": to,
                                "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                                "text": "Novo usuário cadastrado: " + newUser})

    #Parte log do server
    print('Enviando mensagem (Resposta)...' + str(resposta) + ' - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), flush=True)
    return resposta



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role', lazy='joined')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

#Parte do WTF
app.config['SECRET_KEY'] = 'chave forte'

moment = Moment(app)

#Parte Migrate
from flask_migrate import Migrate
migrate = Migrate(app, db)

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    role = SelectField('Informe seu Role', choices = [('Administrator', 'Administrator'), ('Moderator', 'Moderator'), ('User', 'User')])
    submit = SubmitField('Submit')

###########################################################################################################################################

#Essa rota está para uso do forms
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:

            user = User(username=form.name.data, role_id = role_escolhido.id)
            db.session.add(user)
            db.session.commit()
            flash('Adicionado novo usuário')

            print('Novo usuário ativando')
            if app.config['FLASKY_ADMIN']:
                print('Enviando mensagem...', flush=True)
                send_simple_message([app.config['FLASKY_ADMIN'], "flaskaulasweb@zohomail.com"], 'Novo usuário', form.name.data)
                print('Mensagem enviada!...', flush=True)
        else:
            flash('Já conheço ele')
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

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)