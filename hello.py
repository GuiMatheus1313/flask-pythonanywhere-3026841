# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello from Flask From Python and NOW ON GIT HUB!</p><table><tr><td><b>Aluno:</b></td><td>Guilherme Matheus de Jesus de Araujo</td></tr><tr><td><b>Prontuário:</b></td><td>PT3026841</td></tr></table>'


@app.route('/user/<name>')
def hello_world2(name):
    return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>{}</td></tr><tr><td><b>Prontuário:</b></td><td>PT3026841</td></tr></table>'.format(name)
