# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template
from datetime import datetime
from flask_moment import Moment #Perguntar ao professor se o objeto fo flask está vivo na memória para os outros componentes

app = Flask(__name__)

moment = Moment(app)

@app.route('/')
def hello_world():
    name = "eu estou usando o JINJA2!";
    return render_template('template-base.html', current_time = datetime.utcnow());


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