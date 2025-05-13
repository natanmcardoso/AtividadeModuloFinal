#Crie um programa que:
# Crie um menu interativo onde o usuário pode ficar fazendo consultas de notícias
# Pergunte ao usuário um tema de notícia
# Pergunte quantas notícias ele quer buscar sobre o tema, lembre de fazer um limitador
# Busque as N notícias mais recentes sobre o tema usando a API da NewsAPI
# Aprensente as informções de título da notícia , qual a fonte e o nome da pessoa que escreveu, de forma organizada para o usuário
# Armazene o histórico de temas que o usuário buscou e ao sair do menu, apresente no final quais foram as palavras buscadas e quantas notícias foram buscadas no total
# Faça o envio pelo commit do Github

# Importa as bibliotecas necessárias
import requests  # Para realizar requisições HTTP
import os  # Para acessar variáveis de ambiente
import webbrowser  # Para abrir URLs no navegador padrão
from dotenv import load_dotenv  # Para carregar variáveis de ambiente do arquivo .env

# Carrega as variáveis do arquivo .env (incluindo a chave da API)
load_dotenv()
api_key = os.getenv('NEWS_API_KEY')  # Obtém a chave da API de dentro das variáveis de ambiente

# Verifica se a chave da API foi carregada corretamente
if not api_key:
    raise ValueError('API Key não foi localizada nas variáveis de ambiente.')  # Se não encontrar, gera erro

# Define o endpoint da API da NewsAPI
url = "https://newsapi.org/v2/everything"
headers = {'x-api-key': api_key}  # Define os cabeçalhos da requisição, incluindo a chave da API


# Função para buscar notícias com base em um tema, quantidade e idioma
def buscar_noticias(tema, quantidade, idioma):
    params = {
        'q': tema,  # Tema da busca
        'language': idioma,  # Idioma dos resultados
        'pageSize': quantidade,  # Quantidade de notícias a ser retornada
        'sortBy': 'publishedAt'  # Ordena as notícias pela data de publicação
    }

    # Realiza a requisição GET à API da NewsAPI
    resposta = requests.get(url, headers=headers, params=params)

    # Verifica se a requisição foi bem-sucedida (status code 200)
    if resposta.status_code != 200:
        print("Erro ao consultar a API:", resposta.status_code)  # Caso contrário, exibe um erro
        return 0  # Retorna 0 se não houver resultados

    resposta_json = resposta.json()  # Converte a resposta da API para o formato JSON
    artigos = resposta_json.get('articles', [])  # Obtém a lista de artigos (notícias)

    # Itera sobre os artigos encontrados e exibe informações detalhadas
    for artigo in artigos:
        print("\n--------------------------")
        print(f"Título: {artigo.get('title')}")  # Exibe o título da notícia
        print(f"Fonte: {artigo.get('source', {}).get('name')}")  # Exibe a fonte (site)
        print(f"Autor: {artigo.get('author')}")  # Exibe o autor da notícia (se disponível)
        print(f"Abrindo notícia no navegador: {artigo.get('url')}")  # Mostra o link da notícia
        webbrowser.open(artigo.get('url'))  # Abre a notícia no navegador padrão

    return len(artigos)  # Retorna a quantidade de notícias encontradas


# Função principal do menu, onde o usuário interage com o programa
def menu_principal():
    temas_buscados = []  # Lista para armazenar os temas buscados e a quantidade de notícias
    total_noticias = 0  # Contador total de notícias buscadas

    # Dicionário de idiomas suportados pela NewsAPI
    idiomas_disponiveis = {
        'pt': 'Português',
        'en': 'Inglês',
        'es': 'Espanhol',
        'de': 'Alemão',
        'fr': 'Francês',
        'it': 'Italiano',
        'ru': 'Russo'
    }

    # Loop que mantém o menu ativo até o usuário escolher sair
    while True:
        # Exibe o menu com ícones para cada opção
        print("\n=========================")
        print("  📰 Consulta de Notícias  ")
        print("=========================")
        print("1️⃣ - Buscar notícias")
        print("2️⃣ - Mostrar histórico de buscas")
        print("0️⃣ - Sair")
        opcao = input("Escolha uma opção (1, 2 ou 0): ").strip()

        # Se o usuário escolher buscar notícias
        if opcao == '1' or opcao == '1️⃣':
            # Exibe as opções de idiomas antes de perguntar o tema
            print("\nEscolha o idioma para a busca:")
            for code, language in idiomas_disponiveis.items():
                print(f"{code} - {language}")

            # Solicita o idioma desejado
            while True:
                idioma = input("Digite o código do idioma: ").strip().lower()
                if idioma in idiomas_disponiveis:
                    break  # Sai do loop se o idioma for válido
                else:
                    print("⚠️ Idioma inválido. Tente novamente.")

            tema = input("🔍 Digite o tema que deseja buscar: ")  # Solicita o tema para busca

            # Loop para garantir que a quantidade de notícias seja válida
            while True:
                try:
                    quantidade = int(input("📄 Quantas notícias deseja buscar (1 a 20)? "))  # Solicita a quantidade
                    if 1 <= quantidade <= 20:
                        break  # Sai do loop se a quantidade estiver dentro do intervalo
                    else:
                        print("⚠️ Digite um número entre 1 e 20.")
                except ValueError:
                    print("⚠️ Digite um número válido.")  # Caso o usuário não digite um número

            # Chama a função que busca as notícias com o tema, a quantidade e o idioma fornecido
            noticias_encontradas = buscar_noticias(tema, quantidade, idioma)
            temas_buscados.append((tema, noticias_encontradas))  # Adiciona o tema e a quantidade de notícias
            total_noticias += noticias_encontradas  # Atualiza o contador total de notícias

        # Se o usuário escolher mostrar o histórico de buscas
        elif opcao == '2' or opcao == '2️⃣':
            print("\n=== Histórico de Buscas ===")
            if temas_buscados:  # Verifica se há histórico de buscas
                for tema, qtd in temas_buscados:  # Exibe o histórico de buscas
                    print(f"Tema: '{tema}' - {qtd} notícia(s) encontrada(s).")
                print(f"\n📊 Total de notícias buscadas: {total_noticias}")  # Exibe o total de notícias buscadas
            else:
                print("📝 Nenhuma busca realizada ainda.")
        
        # Se o usuário escolher sair
        elif opcao == '0' or opcao == '0️⃣':
            print("\n👋 Encerrando o programa...")
            break  # Sai do loop e encerra o programa

        # Caso o usuário digite uma opção inválida
        else:
            print("❌ Opção inválida. Tente novamente.")  # Exibe uma mensagem de erro

# Chama a função principal para executar o menu
menu_principal()
