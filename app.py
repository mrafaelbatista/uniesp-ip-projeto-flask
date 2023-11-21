import os
from flask import Flask, render_template

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

# Teste de Glossário
glossario = [
    ['Internet', 'Acessar internet'],
    ['Java', 'Pior linguagem de Programação'],
    ['Python', 'Melhor linguagem']
             ]

@app.route('/index_beHealthy.html')
def index_beHealthy():
    return render_template('index_beHealthy.html', glossario=glossario)


@app.route('/cadastro_beHealthy.html')
def cadastro_beHealthy():
    return render_template('cadastro_beHealthy.html')


@app.route('/login_beHealthy.html')
def login_beHealthy():
    return render_template('login_beHealthy.html')


if __name__ == "__main__":
    app.run()
