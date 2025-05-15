## Crie um programa que utilize a API do Jsonplaceholder:
## Permita um menu interativo onde o usuário possa:
## Primeiro, se identificar e, com isso, fazer uma verificação se usuário existe (tenha um dicionário simulando um banco de dados com código, e-mail e senha, por exemplo).
## Após login, permita a ele: visualizar posts e comentários.
## Visualizar seus próprios posts.
## Filtrar posts por algum outro usuário.
## Criar um novo post (usar usuário logado).
## Exibir um resumo das interações feitas ao sair do laço (quantos posts e comentários foram visualizados e quantos posts foram criados por ele).

# Importa bibliotecas necessárias
import requests

# Simula um banco de dados de usuários
usuarios = {
    "1": {"email": "natan@mail.com", "senha": "admin"},
    "2": {"email": "alfonso@mail.com", "senha": "password"},
}

# Lista para armazenar os posts criados na sessão
posts_criados_localmente = []

# Função para autenticar usuário
def autenticar():
    print("===== Login =====")
    codigo = input("Código do usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")

    if codigo in usuarios and usuarios[codigo]['email'] == email and usuarios[codigo]['senha'] == senha:
        print("\n✅ Login bem-sucedido!")
        return int(codigo)
    else:
        print("\n❌ Usuário ou senha inválidos.")
        return None

# Função para buscar todos os posts
def visualizar_posts():
    resposta = requests.get("https://jsonplaceholder.typicode.com/posts")
    if resposta.status_code == 200:
        posts = resposta.json()
        for post in posts[:5]:
            print(f"\033[94m\n(Post da API)\033[0m\nPost ID: {post['id']}\nTítulo: {post['title']}\nConteúdo: {post['body']}")
        return 5
    else:
        print("Erro ao buscar posts.")
        return 0

# Função para visualizar comentários de um post
def visualizar_comentarios():
    post_id = input("Digite o ID do post para ver os comentários: ")
    resposta = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if resposta.status_code == 200:
        comentarios = resposta.json()
        for comentario in comentarios:
            print(f"\nAutor: {comentario['email']}\nComentário: {comentario['body']}")
        return len(comentarios)
    else:
        print("Erro ao buscar comentários.")
        return 0

# Função para visualizar os próprios posts
def visualizar_meus_posts(user_id):
    total = 0

    for i, post in enumerate(posts_criados_localmente):
        if post['userId'] == user_id:
            print(f"\033[92m\n(Post Local #{i})\033[0m\nTítulo: {post['title']}\nConteúdo: {post['body']}")
            total += 1

    if total == 0:
        print("\n⚠️ Nenhum post criado por você nesta sessão.")

    return total

# Função para editar post local
def editar_post(user_id):
    visualizar_meus_posts(user_id)
    try:
        index = int(input("\nDigite o número do post que deseja editar: "))
        post = posts_criados_localmente[index]
        if post['userId'] != user_id:
            print("❌ Você só pode editar seus próprios posts.")
            return 0
        novo_titulo = input("Novo título: ")
        novo_corpo = input("Novo conteúdo: ")
        post['title'] = novo_titulo
        post['body'] = novo_corpo
        print("✅ Post editado com sucesso!")
        return 1
    except (IndexError, ValueError):
        print("❌ Post não encontrado.")
        return 0

# Função para deletar post local
def deletar_post(user_id):
    visualizar_meus_posts(user_id)
    try:
        index = int(input("\nDigite o número do post que deseja deletar: "))
        post = posts_criados_localmente[index]
        if post['userId'] != user_id:
            print("❌ Você só pode deletar seus próprios posts.")
            return 0
        posts_criados_localmente.pop(index)
        print("✅ Post deletado com sucesso!")
        return 1
    except (IndexError, ValueError):
        print("❌ Post não encontrado.")
        return 0

# Função para filtrar posts por outro usuário
def filtrar_posts():
    user_id = input("Digite o ID do usuário para ver os posts: ")
    if user_id not in usuarios:
        print("❌ Usuário não encontrado.")
        return 0

    resposta = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    if resposta.status_code == 200:
        posts = resposta.json()
        for post in posts:
            print(f"\033[94m\n(Post da API)\033[0m\nPost ID: {post['id']}\nTítulo: {post['title']}\nConteúdo: {post['body']}")
        return len(posts)
    else:
        print("Erro ao buscar posts do usuário.")
        return 0

# Função para criar um novo post
def criar_post(user_id):
    titulo = input("Digite o título do post: ")
    corpo = input("Digite o conteúdo do post: ")
    novo_post = {
        "title": titulo,
        "body": corpo,
        "userId": user_id
    }
    resposta = requests.post("https://jsonplaceholder.typicode.com/posts", json=novo_post)
    if resposta.status_code == 201:
        print("\n✅ Post criado com sucesso!")
        posts_criados_localmente.append(novo_post)
        return 1
    else:
        print("Erro ao criar o post.")
        return 0

# Execução principal do programa (sem usar if __name__ == '__main__')
usuario_logado = None
while usuario_logado is None:
    usuario_logado = autenticar()

interacoes = {
    "posts_visualizados": 0,
    "comentarios_visualizados": 0,
    "meus_posts_visualizados": 0,
    "posts_filtrados": 0,
    "posts_criados": 0,
    "posts_editados": 0,
    "posts_deletados": 0
}

while True:
    print("\n===== MENU =====")
    print("1️⃣  Visualizar posts da API")
    print("2️⃣  Visualizar comentários de um post")
    print("3️⃣  Criar novo post")
    print("4️⃣  Ver meus posts")
    print("5️⃣  Editar um post meu")
    print("6️⃣  Deletar um post meu")
    print("7️⃣  Filtrar posts de outro usuário")
    print("0️⃣  Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        interacoes['posts_visualizados'] += visualizar_posts()
    elif opcao == "2":
        interacoes['comentarios_visualizados'] += visualizar_comentarios()
    elif opcao == "3":
        interacoes['posts_criados'] += criar_post(usuario_logado)
    elif opcao == "4":
        interacoes['meus_posts_visualizados'] += visualizar_meus_posts(usuario_logado)
    elif opcao == "5":
        interacoes['posts_editados'] += editar_post(usuario_logado)
    elif opcao == "6":
        interacoes['posts_deletados'] += deletar_post(usuario_logado)
    elif opcao == "7":
        interacoes['posts_filtrados'] += filtrar_posts()
    elif opcao == "0":
        print("\n👋 Saindo do programa...")
        break
    else:
        print("Opção inválida.")

print("\n===== RESUMO DAS INTERAÇÕES =====")
print(f"Posts visualizados: {interacoes['posts_visualizados']}")
print(f"Comentários visualizados: {interacoes['comentarios_visualizados']}")
print(f"Posts criados: {interacoes['posts_criados']}")
print(f"Seus posts visualizados: {interacoes['meus_posts_visualizados']}")
print(f"Posts editados: {interacoes['posts_editados']}")
print(f"Posts deletados: {interacoes['posts_deletados']}")
print(f"Posts de outros usuários visualizados: {interacoes['posts_filtrados']}")