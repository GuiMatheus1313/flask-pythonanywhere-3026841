# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "eu estou usando o JINJA2!";
    return render_template('template-base.html');


@app.route('/user/<name>')
def hello_pront(name):
    name2 = name
    return render_template('user.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404;

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return '<h1>Dados pelo Contexto!</h1>Browser: {}</p><br><p>IP_cliente: {}</p><br><p>Host: {}</p>'.format(navegador,Ip_remoto,host_name)