from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota para cadastrar uma nova notícia
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Obtém os dados do formulário
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']

        # Abre o arquivo JSON
        with open('noticias.json', 'r') as file:
            # Lê o conteúdo do arquivo JSON
            dados = json.load(file)

        # Obtém a lista de notícias
        noticias = dados.get('noticias', [])

        # Obtém o próximo ID disponível
        proximo_id = len(noticias) + 1

        # Cria um novo objeto de notícia
        nova_noticia = {
            'id': proximo_id,
            'titulo': titulo,
            'conteudo': conteudo
        }

        # Adiciona a nova notícia à lista
        noticias.append(nova_noticia)

        # Atualiza os dados no arquivo JSON
        dados['noticias'] = noticias
        with open('noticias.json', 'w') as file:
            json.dump(dados, file, indent=4)

        return redirect('/cadastrar')

    return render_template('cadastrar.html')

# Rota para exibir as notícias cadastradas
@app.route('/noticias')
def noticias():
    # Abre o arquivo JSON
    with open('noticias.json', 'r') as file:
        # Lê o conteúdo do arquivo JSON
        dados = json.load(file)

    # Obtém a lista de notícias
    noticias = dados.get('noticias', [])

    return render_template('noticias.html', noticias=noticias)


# Rota adms
@app.route('/adms')
def adms():
    return render_template('adms.html')




if __name__ == '__main__':
    app.run(debug=True)


