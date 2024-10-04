# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Avaliação contínua: Aula 030</h1><br><ul><li><a href="/">Home</a></li><li><a href="/user/GuiMatheus/PT3026841/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></u>'



@app.route('/user/<name>/<pront>/<inst>')
def hello_pront(name, pront, inst):
    return '<h1>Dados pela URL!</h1><table><tr><td><b>Aluno:</b></td><td>{}</td></tr><tr><td><b>Prontuário:</b></td><td>{}</td></tr><td><b>Instituição:</b></td><td>{}</td></tr></table>'.format(name, pront, inst)

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return '<h1>Dados pelo Contexto!</h1>Browser: {}</p><br><p>IP_cliente: {}</p><br><p>Host: {}</p>'.format(navegador,Ip_remoto,host_name)


