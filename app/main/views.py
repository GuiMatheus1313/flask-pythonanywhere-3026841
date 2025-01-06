from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, flash, request
from . import main
from .forms import NameForm
from .. import db #está voltando duas pastas
from ..models import User, Role
from ..email import send_email, send_simple_message


@main.route('/', methods=['GET', 'POST'])
def hello_world():
    form = NameForm()
    all_user = User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            role_user = Role.query.filter(Role.name == 'User').first()
            user = User(username=form.name.data, role_id=role_user.id)
            db.session.add(user)
            db.session.commit()
            flash('Adicionado novo usuário')
            session['checkemail'] = form.email_choice.data
            if current_app.config['FLASKY_ADMIN']:
                #send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
                print('Enviando mensagem...', flush=True)
                send_simple_message([current_app.config['FLASKY_ADMIN'], "flaskaulasweb@zohomail.com"], 'Novo usuário', form.name.data)
                print('Mensagem enviada...', flush=True)
        else:
            flash('Já conheço ele')
            session['checkemail'] = ''
        session['name'] = form.name.data
        return redirect(url_for('main.hello_world'))
    return render_template('formularioTeste.html', form = form, name = session.get('name'), checkemail = session.get('checkemail'), pessoa = all_user)

@main.route('/user/<name>')
def hello_pront(name):
    name2 = name
    return render_template('user.html', name = name, pront = 'PT3026841', ins = 'IFSP' , current_time = datetime.utcnow())
@main.errorhandler(404)
def not_found(e):
    return render_template('404.html', current_time = datetime.utcnow()), 404;
@main.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return render_template('contextorequisicao.html', name = 'Guilherme', navegador = navegador, IP_cliente = Ip_remoto, host_name = host_name);