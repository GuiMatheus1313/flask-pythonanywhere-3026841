# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "eu estou usando o JINJA2!";
    return render_template('index.html');


@app.route('/user/<name>/<pront>/<inst>')
def hello_pront(name, pront, inst):
    return '<h1>Dados pela URL!</h1><table><tr><td><b>Aluno:</b></td><td>{}</td></tr><tr><td><b>Prontuário:</b></td><td>{}</td></tr><td><b>Instituição:</b></td><td>{}</td></tr></table>'.format(name, pront, inst)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404;

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return '<h1>Dados pelo Contexto!</h1>Browser: {}</p><br><p>IP_cliente: {}</p><br><p>Host: {}</p>'.format(navegador,Ip_remoto,host_name)