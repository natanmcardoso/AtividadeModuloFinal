# Consulta de Notícias

Este é um programa em Python que permite buscar notícias de diferentes fontes e idiomas utilizando a [NewsAPI](https://newsapi.org/). O programa oferece um menu interativo, onde o usuário pode escolher o idioma da pesquisa, o tema das notícias e a quantidade de resultados que deseja receber.

## Funcionalidades

- **Buscar notícias**: Permite ao usuário buscar notícias com base em um tema específico e escolher o idioma para a busca.
- **Histórico de buscas**: Mostra o histórico das buscas realizadas, com o tema e a quantidade de notícias encontradas.
- **Abertura de notícias**: As notícias encontradas são abertas diretamente no navegador.

## Como usar

### Pré-requisitos

Antes de rodar o programa, é necessário ter o Python instalado em sua máquina e as dependências do projeto configuradas.

1. Instale o Python (caso ainda não tenha).
2. Instale as dependências necessárias com o seguinte comando:

```bash
pip install requests python-dotenv
```

3. Crie um arquivo `.env` na raiz do projeto e insira sua chave de API da NewsAPI. Exemplo:

```text
NEWS_API_KEY=your_api_key_here
```

Para obter sua chave de API, acesse [NewsAPI](https://newsapi.org/).

### Rodando o programa

Após configurar o arquivo `.env`, você pode executar o programa com o seguinte comando:

```bash
python main.py
```

### Menu interativo

O programa apresenta um menu onde você pode escolher as seguintes opções:

1. **Buscar notícias**: Você pode buscar notícias informando o idioma, o tema e a quantidade de notícias desejadas.
2. **Mostrar histórico de buscas**: Exibe o histórico das buscas realizadas até o momento.
3. **Sair**: Encerra o programa.

### Exemplo de Execução

=========================
  📰 Consulta de Notícias  
=========================
1️⃣ - Buscar notícias
2️⃣ - Mostrar histórico de buscas
0️⃣ - Sair
Escolha uma opção (1, 2 ou 0): 1
Escolha o idioma para a busca:
pt - Português
en - Inglês
es - Espanhol
de - Alemão
fr - Francês
it - Italiano
ru - Russo
Digite o código do idioma: pt
🔍 Digite o tema que deseja buscar: tecnologia
📄 Quantas notícias deseja buscar (1 a 20)? 5
--------------------------
Título: "Notícia sobre tecnologia"
Fonte: "TechCrunch"
Autor: "John Doe"
Abrindo notícia no navegador: https://example.com
```

## Estrutura do Projeto

- **`main.py`**: Contém o código principal do programa, incluindo a interação com a API e o menu interativo.
- **`.env`**: Arquivo onde a chave da API da NewsAPI deve ser armazenada.

## Licença

Este projeto é de código aberto e pode ser utilizado de acordo com os termos da licença MIT.
