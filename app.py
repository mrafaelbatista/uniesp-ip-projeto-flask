import os
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


@app.route('/')
def index_beHealthy():
    return render_template('index_beHealthy.html')


@app.route('/cadastro_beHealthy')
def cadastro_beHealthy():
    return render_template('cadastro_beHealthy.html')


@app.route('/processar_cadastro', methods=['POST'])
def processar_cadastro():
    if request.method == 'POST':
        # Obtém os dados do formulário
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')

        # Caminho para o arquivo CSV
        dados_cadastro = 'dados_cadastro.csv'

        # Verifica se o arquivo já existe
        arquivo_existe = os.path.exists(dados_cadastro)

        # Abre o arquivo CSV em modo de escrita
        with open(dados_cadastro, 'a', newline='') as csvfile:
            # Cria um objeto de gravação CSV
            csv_writer = csv.writer(csvfile)

            # Se o arquivo não existir, escreve o cabeçalho
            if not arquivo_existe:
                csv_writer.writerow(['Email', 'Senha', 'Telefone'])

            # Escreve os dados no arquivo CSV
            csv_writer.writerow([email, senha, telefone])

        return render_template('cadastro_beHealthy.html', mensagem='Cadastro realizado com sucesso!')


@app.route('/login_beHealthy')
def login_beHealthy():
    return render_template('login_beHealthy.html')


def verificar_login(email, senha):
    with open('dados_cadastro.csv', 'r', newline='') as arquivo:
        # Cria um leitor
        csv_reader = csv.reader(arquivo)

        # Ignora o cabeçalho se existir
        next(csv_reader, None)

        for linha in csv_reader:
            email_arquivo, senha_arquivo, _ = linha
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


@app.route('/index2_beHealthy')
def index2_beHealthy():
    return render_template('index2_beHealthy.html')


@app.route('/receitas', methods=['GET'])
def listar_receitas():
    # Caminho para o arquivo CSV
    cadastro_receitas_lista = 'cadastro_receitas.csv'

    # Verifica se o arquivo existe
    arquivo_existe_receita = os.path.exists(cadastro_receitas_lista)

    # Se o arquivo não existir ou estiver vazio, retorna uma lista vazia
    if not arquivo_existe_receita or os.stat(cadastro_receitas_lista).st_size == 0:
        receitas_lista = []
    else:
        # Abre o arquivo CSV em modo de leitura
        with open(cadastro_receitas_lista, 'r', newline='') as csvfile_lista:
            # Cria um objeto de leitura CSV
            csv_reader = csv.reader(csvfile_lista)
            # Ignora o cabeçalho se existir
            next(csv_reader, None)
            # Lê as receitas do arquivo CSV
            receitas_lista = list(csv_reader)

    return render_template('receitas.html', receitas=receitas_lista)


@app.route('/form_cadastro_receita')
def form_cadastro_receita():
    return render_template('form_cadastro_receita.html')


@app.route('//processar_cadastro_receita', methods=['POST'])
def processar_cadastro_receita():
    if request.method == 'POST':
        # Obtém os dados do formulário
        titulo_receita = request.form.get('titulo_receita')
        ingredientes_receita = request.form.get('ingredientes_receita')

        # Caminho para o arquivo CSV
        cadastro_receitas = 'cadastro_receitas.csv'

        # Verifica se o arquivo já existe
        arquivo_existe = os.path.exists(cadastro_receitas)

        # Abre o arquivo CSV em modo de escrita
        with open(cadastro_receitas, 'a', newline='') as csvfile:
            # Cria um objeto de gravação CSV
            csv_writer = csv.writer(csvfile)

            # Se o arquivo não existir, escreve o cabeçalho
            if not arquivo_existe:
                csv_writer.writerow(['titulo_receita', 'ingredientes_receita'])

            # Escreve os dados no arquivo CSV
            csv_writer.writerow([titulo_receita, ingredientes_receita])

        return render_template('form_cadastro_receita.html', mensagem='Cadastro de receita realizado com sucesso!')


if __name__ == "__main__":
    app.run()
