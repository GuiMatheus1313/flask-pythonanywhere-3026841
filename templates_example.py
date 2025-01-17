# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template, session, url_for, redirect, flash, abort
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

app = Flask(__name__, template_folder='/home/GuiMatheus1313/myfinal/templates')

#parte SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Disci(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    name = db.Column(db.String(64), unique = True)
    alunos = db.relationship('Aluno', backref='disciplinas', lazy='joined')

    def __repr__(self):
        return '<Disci %r>' % self.name

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), unique = True, index = True)
    disci_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))

    def __repr__(self):
        return '<Aluno %r>' % self.name

#Parte do WTF
app.config['SECRET_KEY'] = 'chave forte'

moment = Moment(app)

#Parte Migrate
from flask_migrate import Migrate
migrate = Migrate(app, db)

class AlunoForm(FlaskForm):
    name = StringField('Qual teu nome?', validators = [DataRequired()])
    disci = SelectField('Informe sua disciplina', choices = [('DSWA5', 'DSWA5'), ('GPSA5', 'GPSA5'), ('IHCA5', 'IHCA'), ('SODA5', 'SODA5'), ('PJIA5', 'PJIA5'), ('TCOA5', 'TCOA5')])
    submit = SubmitField('Cadastrar')





@app.route('/')
def hello_world():
    return render_template('index.html', current_time = datetime.utcnow());



#Essa rota está para uso do forms
@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    form = AlunoForm()
    all_user = Aluno.query.all()
    if form.validate_on_submit():
        user = Aluno.query.filter_by(name=form.name.data).first()
        if user is None:
            disci_escolhida = Disci.query.filter_by(name = form.disci.data).first()
            if disci_escolhida:
                user = Aluno(name=form.name.data, disci_id = disci_escolhida.id)
                db.session.add(user)
                db.session.commit()
                flash('Adicionado novo aluno')
            else:
                flash('Já conheço ele')
        else:
            flash('Já conheço ele')
        return redirect(url_for('alunos'))
    return render_template('formularioTeste.html', form = form, pessoa = all_user)


@app.errorhandler(404)
def not_found_404(e):
    return render_template('404.html', current_time = datetime.utcnow()), 404;

@app.route('/404')
def not_found():
    abort(404)

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return render_template('contextorequisicao.html', name = 'Guilherme', navegador = navegador, IP_cliente = Ip_remoto, host_name = host_name);

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Aluno=Aluno, Disci=Disci)