
# Consulta de Notícias - Programa para buscar notícias da NewsAPI

Este programa permite buscar notícias de diversos temas utilizando a API da NewsAPI, além de armazenar o histórico das buscas realizadas. Ele possui um menu interativo com opções para realizar novas buscas, visualizar o histórico de buscas e encerrar o programa.

## Funcionalidades

- Buscar notícias por tema e idioma.
- Limitar a quantidade de notícias retornadas.
- Exibir informações detalhadas das notícias, incluindo título, fonte, autor e link.
- Armazenar o histórico de buscas realizadas e mostrar o total de notícias buscadas.

## Requisitos

- Python 3.x
- Biblioteca `requests` para realizar requisições HTTP.
- Biblioteca `dotenv` para carregar as variáveis de ambiente.
- Uma chave de API da NewsAPI, que pode ser obtida em [NewsAPI](https://newsapi.org/).

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/consulta-noticias.git
cd consulta-noticias
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` e adicione sua chave da API da NewsAPI:

```bash
NEWS_API_KEY=your_api_key_here
```

4. Execute o programa:

```bash
python consulta_noticias.py
```

## Exemplo de Execução

### Menu de Opções:

```
=========================
  📰 Consulta de Notícias  
=========================
1️⃣ - Buscar notícias
2️⃣ - Mostrar histórico de buscas
0️⃣ - Sair
Escolha uma opção (1, 2 ou 0): 
```

### Buscando notícias:

```
Escolha o idioma para a busca:
pt - Português
en - Inglês
es - Espanhol
de - Alemão
fr - Francês
it - Italiano
ru - Russo
Digite o código do idioma: pt
🔍 Digite o tema que deseja buscar: Inteligência Artificial
📄 Quantas notícias deseja buscar (1 a 20)? 5
--------------------------
Título: Como a Inteligência Artificial está mudando a indústria
Fonte: TechCrunch
Autor: John Doe
Abrindo notícia no navegador: https://example.com
--------------------------
Título: O futuro da Inteligência Artificial na saúde
Fonte: The Verge
Autor: Jane Doe
Abrindo notícia no navegador: https://example.com
```

### Histórico de Buscas:

```
=== Histórico de Buscas ===
Tema: 'Inteligência Artificial' - 5 notícia(s) encontrada(s).
📊 Total de notícias buscadas: 5
```

### Fechamento do Programa:

```
👋 Encerrando o programa...
```

## Contribuições

Se você deseja contribuir com melhorias, sugestões ou correções, fique à vontade para enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
