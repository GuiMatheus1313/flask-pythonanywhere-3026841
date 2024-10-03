# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello from Flask From Python and NOW ON GIT HUB!</p><table><tr><td><b>Aluno:</b></td><td>Guilherme Matheus de Jesus de Araujo</td></tr><tr><td><b>Prontuário:</b></td><td>PT3026841</td></tr></table>'


@app.route('/user/<name>')
def hello_world2(name):
    return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>{}</td></tr><tr><td><b>Prontuário:</b></td><td>PT3026841</td></tr></table>'.format(name)
"""
teste
@app.route('/contextoderequisicao')
def contexto():
    user_agent = request.headers.get('User-Agent')
    return '<p>{}</p>'.format(user_agent)

@app.route('/codigostatusdiferente')
def statuscode():
    response = make_response('<p>Bad Request</p>', 400)
    return response

@app.route('/objetoresposta')
def objectresponse():
    response = make_response('<p>Oi, tem um cookie em mim mesmo</p>', 400)
    response.set_cookie("chave", "35")
    return response

#EXEMPLO DE FAZER UM COOKIE

resp.set_cookie(
        'meu_cookie',
        'valor_do_cookie',
        max_age=60*60*24,  # 1 dia
        expires='Fri, 31-Dec-2023 23:59:59 GMT',  # Data específica
        path='/',
        secure=True,
        httponly=True,
        samesite='Lax'
    )


@app.route('/redirecionamento')
def redirection():
    return redirect('https://ptb.ifsp.edu.br/')

@app.route('/abortar')
def aborta():
    return abort(403)
"""



