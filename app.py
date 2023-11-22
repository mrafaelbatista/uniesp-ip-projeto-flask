import os
from flask import Flask, render_template, request

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

@app.route('/')
def index_beHealthy():
    return render_template('index_beHealthy.html', glossario=glossario)


@app.route('/cadastro_beHealthy.html')
def cadastro_beHealthy():
    return render_template('cadastro_beHealthy.html')


@app.route('/processar_cadastro', methods=['POST'])
def processar_cadastro():
    if request.method == 'POST':
        # Obtém os dados do formulário
        email = request.form.get('email')  # 'email' é o nome do campo no formulário
        senha = request.form.get('senha')  # 'senha' é o nome do campo no formulário
        telefone = request.form.get('telefone')  # 'telefone' é o nome do campo no formulário

        # Salva os dados em um arquivo .txt
        with open('dados_cadastro.txt', 'a') as arquivo:
            arquivo.write(f'Email: {email}, Senha: {senha}, Telefone: {telefone}\n')

        return render_template('cadastro_beHealthy.html', mensagem='Cadastro realizado com sucesso!')


@app.route('/login_beHealthy.html')
def login_beHealthy():
    return render_template('login_beHealthy.html')


if __name__ == "__main__":
    app.run()
