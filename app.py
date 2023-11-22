import os
from flask import Flask, render_template, request, redirect, url_for

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


def verificar_login(email, senha):
    with open('dados_cadastro.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(', ')
            email_arquivo = dados[0].split(': ')[1]
            senha_arquivo = dados[1].split(': ')[1]
            if email == email_arquivo and senha == senha_arquivo:
                return True
    return False


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        if verificar_login(email, senha):
            return redirect(url_for('index2_beHealthy'))
        else:
            mensagem_erro = "Usuário ou senha incorretos. Por favor, tente novamente."
            return render_template('login_beHealthy.html', mensagem_erro=mensagem_erro)


@app.route('/index2_beHealthy.html')
def index2_beHealthy():
    return render_template('index2_beHealthy.html')


if __name__ == "__main__":
    app.run()
