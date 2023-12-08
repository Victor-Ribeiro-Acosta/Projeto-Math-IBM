
"""Programa Match - IBM/MasterTech
Módulo 2

Alunos:
Roger Oliveira
Victor Acosta
Patrícia

Trabalho de Conclusão de Curso

Projeto 3: Catálogo de Livros com Verificação de Disponibilidade

Neste projeto, os alunos criarão um catálogo de livros em Python. A aplicação incluirá as
seguintes etapas:
➔ Cadastro de Livros:
◆ Os usuários poderão cadastrar livros, incluindo título, autor e número de
exemplares disponíveis.
➔ Validação de Disponibilidade:
◆ A aplicação verificará se o número de exemplares disponíveis é um valor
válido e maior que zero.

➔ Pesquisa de Livros:
◆ Os usuários poderão pesquisar livros por título ou autor.
◆ A aplicação exibirá os resultados da pesquisa e a disponibilidade de cada
livro. """



# "Matchlivros", uma pequena biblioteca comunitária'

"""Apresentação:

A execução de um catálogo de livros, por si só, seria um exercício técnico, 
sem uma aplicabilidade imediata.
Decidimos dar uma alma ao cadastro, desenvolvendo a "Matchlivros", uma biblioteca pequena,
para uso de quaisquer tipos de pequanas comunidades, que contendo livros impressos, terá papel
essencial não apenas no desenvolvimento cultural onde está inserida e arredores,mas também 
na integr:ação dos seus membros e moradores vizinhos. Neste momento, an leitura será somente 
na sede da biblioteca.
 
Apresentação técnica: Desenvolvida em linguagem de programação Python 3, utilizamos uma parte 
do conteúdo apresentado em aulas, bem como conhecientos adquiridos em pesquisas na web. 
Foram utilizadas variáveis, funções, Listas, bibliotecas, classes, operações aritméticas, inputs,
prints, strigs, condicionais e outros elementos de Python. 
Devido ao tempo exíguo, a interface é padrão da  IDE que executa o programa.

O futuro: 
Será desenvolvida uma interface gráfica adequada, responsiva, agradável e útil, dentro 
dos padrões do Design da Experiência de Usuárioe Design de Interface de Usuário.

Serão implementadas as funcionalidades para:
--Integração com banco de dados
--Reserva de livros
--Empréstimo de livros
--Comunicação de Extravio
--Integração com a IA
--Acesso também por bot no whatsapp 
"""



# Importando o módulo os
import os

# Variável para a senha do administrador
admsenha = "315315315mn@"

# Classe para o usuário
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

# Classe para o livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

# Classe para a biblioteca
class Biblioteca:
    def __init__(self):
        self.usuarios = {}
        self.livros = {}

    def cadastrar_usuario(self, usuario):
        if len(self.usuarios) < 50:
            self.usuarios[usuario.nome] = usuario
            print("\nVocê foi cadastrado na Matchlivros, agora faça um login!")
            return True
        else:
            print("Desculpe, já atingimos o limite de 50 usuários.")
            return False

    def descadastrar_usuario(self, nome):
        if nome in self.usuarios:
            del self.usuarios[nome]
            print("Usuário descadastrado com sucesso!")
        else:
            print("Não conseguimos achar você por este nome.")

    def cadastrar_livro(self, livro):
        if livro.titulo in self.livros:
            resposta = input(f"\nEste título já está em nosso  cadastro.\n Você quer doar um exemplar dele  (S/N): ").lower()
            if resposta == "s":
                try:
                    quantidade = int(input("Quantos livros você quer doar? "))
                    self.livros[livro.titulo].quantidade += quantidade
                    print(f"A quantidade de exemplares de '{livro.titulo}' agora é de {self.livros[livro.titulo].quantidade}.")
                except ValueError:
                    print('  ')
                    print("Houve algum problema com a quantidade, melhor revisar.")
            else:
                print("Cadastro cancelado.")
        else:
            self.livros[livro.titulo] = livro
            print('  ')
            print("Este livro foi cadastrado com sucesso!")

# Dicionário para armazenar usuários e livros
usuarios = {}
livros = {}
biblioteca = Biblioteca()

# Lista de gêneros
generos = [
    "artes", "autoajuda", "aventura", "biografia", "ciências", "comédia",
    "conto", "crônica", "documentário", "drama histórico", "educação",
    "elegia", "ensaio", "fantasia", "farsa", "ficção", "ficção científica",
    "ficção de aventura", "ficção de espionagem", "ficção especulativa",
    "ficção histórica", "ficção para jovens adultos", "ficção policial",
    "haicai", "história", "jornalismo literário", "light novel",
    "literatura infantil", "livros de receitas", "livros de referência",
    "livros ilustrados", "lírico", "melodrama", "memórias", "mangá",
    "mistério", "música", "novela", "ode", "realismo mágico", "romance",
    "soneto", "suspense", "tecnologia", "terror", "tragédia"
]

# Função para imprimir lista com quebras de linha
def imprimir_lista_quebrada(lista):
    for genero in lista:
        print(genero)

# Função para cancelar e voltar ao menu inicial
def cancelar(menu):
    
    resposta = input("\nQuer voltar ao menu inicial? (S/N): ").lower()
    if resposta in ("s", "sim"):
        main() 
    else:
        return
    

# Função para encontrar o gênero mais parecido na lista de gêneros
def encontrar_genero(genero):
    
    for g in generos:
        if g.startswith(genero.lower()[:4]):
            return g
    return genero

# Função para cadastrar usuário
def cadastrar_usuario():

    # Input da Senha
    tentativas = 0
    while tentativas < 5:
        nome = input("Escreva o seu nome de usuário: ")
        if len(nome) <= 45 and nome.replace(' ', '').isalpha():
            break
        else:
            print("O seu nome deve conter até 45 letras e espaços. Tente novamente.")
            tentativas += 1
    if tentativas == 5:
        print("Tentativas demais, vamos voltar para o menu.")
        return False

    tentativas = 0
    while tentativas < 10:
        senha = input("Digite uma senha com 5 dígitos: ")
        if len(senha) == 5 and senha.isalnum():
            for usuario in biblioteca.usuarios.values():
                if usuario.senha == senha:
                    print("Esta senha já está em uso. Por favor, digite outra senha.")
                    break
            else:
                usuario = Usuario(nome, senha)
                if biblioteca.cadastrar_usuario(usuario):
                    return True
        elif len(senha) <= 4:
            print("É obrigatório que a senha tenha 5 dígitos")
        else:
            print("A senha deve conter somente letras e números. Tente novamente.")

        tentativas += 1
        if tentativas == 9:
            print("A próxima tentativa é a última.")
    if tentativas == 10:
        print("Número máximo de tentativas atingido. Retornando ao menu principal.")
        return False

# Função para login do usuário
def login():
    
    global usuario_logado
    nome = input("Digite o seu nome de usuário: ")
    if nome in biblioteca.usuarios:
        if 'usuario_logado' in globals() and usuario_logado == nome:
            print(f"Você já está logado,!")
            return True
        else:
            senha = input("Digite a sua senha de 5 dígitos: ")
            if biblioteca.usuarios[nome].senha == senha:
                usuario_logado = nome
                print(f"\nBem vindo, {nome}!\n____________________")
                return True
            else:
                print("A sua senha não está certa, tente novamente.")
                return False
    else:
        print("Parece que o seu nome ou a sua senha não estão aqui.")
        return False

# Função para descadastrar usuário com verificação de login e senha do administrador
def descadastrar_usuario():
    
    print("Fale com o administrador antes de continuar")
    print("________________________________________________________\n")

    # Chama a função cancelar antes de interagir com o administrador
    cancelar("Fale com o administrador antes de continuar? (S/N)")

    nome = input("Se você não quer mais ter acesso a MatchLivros, digite o seu nome: ")
    if nome in biblioteca.usuarios:
        senha = input("Digite a sua senha de 5 dígitos: ")
        if biblioteca.usuarios[nome].senha == senha:
            for i in range(5):
                senha_admin = input("Digite a senha do administrador: ")
                if senha_admin == admsenha:
                    del biblioteca.usuarios[nome]
                    print("A gente espera que um dia você retorne.")
                    return
                else:
                    print("A senha que você digitou não serve... Tente novamente:")
            print("Número máximo de tentativas atingido. Retornando ao menu principal.")
        else:
            print("A senha não está correta, tente novamente:")
    else:
        print("Usuário não encontrado.")

# Função para cadastrar livro
def cadastrar_livro(): 
    
    while True:
        titulo = input("Digite o nome(título) do livro que você quer cadastrar ou doar: ")
        if len(titulo) <= 60:
            break
        else:
            print("O título do livro deve ter até 60 caracteres. Tente novamente:")
    while True:
        autor = input("Agora cadastre o nome do autor: ")
        if len(autor) <= 45:
            break
        else:
            print("O nome do autor deve ter até 45 caracteres. Tente novamente:")
    while True:
        sugestao_genero = input("Você deseja sugestões de gênero? (S/N): ").lower()
        if sugestao_genero in ("s", "sim"):
            print(f"Sugestões de gênero disponíveis: {generos}")
            genero = input("Digite o gênero do livro: ")
        else:
            genero = input("Digite o gênero do livro: ")

        if len(genero) <= 20 and genero.isalpha():
            genero = encontrar_genero(genero)
            break
        else:
            print("Gênero inválido. Por favor, insira um gênero válido sem números e com até 20 caracteres.")

    quantidade = 0  # Inicializamos a quantidade como 0 para novos cadastros
    if titulo in biblioteca.livros:  # Se o livro já existe, pede para adicionar quantidade
        resposta = input(f"O livro '{titulo}' já está no cadastro. Você quer doar um exemplar para a Matchlivros? (S/N): ").lower()
        if resposta in ("s", "sim"):
            try:
                quantidade = int(input("Digite a quantidade de exemplares que você está doando: "))
                biblioteca.livros[titulo].quantidade += quantidade
                
                print(f"\nAgora a Matchlivros tem {biblioteca.livros[titulo].quantidade} exemplares do livro {titulo} .")
                return
            except ValueError:
                print("\nHouve algum problema com a quantidade digitada, tivemos que cancelar..")
        else:
            print("\nA gente não conseguiu cadastrar.")
    else:  # Se o livro não existe, pede a quantidade normalmente
        while True:
            try:
                quantidade = int(input("Quantos exemplares do livro você está cadastrando ou doando? "))
                if 0 <= quantidade <= 100:
                    break
                else:
                    print("Houve agum problema com a quantidade digitada...\nPor favor, insira um número inteiro de 1 a 100.")
            except ValueError:
                print("Parece que você não digitou um número...digite um número inteiro.")

    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.cadastrar_livro(livro)

    
# Função para descadastrar livro com verificação de login e senha do administrador
""" A funcionalidade para escolha de apenas retirar uma quantidade livros, além da função de descadastrar, faremos quando
implantarmos Função de reservar, tomar emprestado, dar baixa em exemplares de um título 
e na Comunicação de Extravio de livros"""
def descadastrar_livro():
    print("\nFale com o administrador antes de continuar,\npois você precisa da autorização dele. ")

    # Chama a função cancelar antes de interagir com o administrador
    cancelar("Entre em contato com o administrador antes de continuar? (S/N)")

    nome = input("Digite o seu nome de usuário: ")
    if nome in biblioteca.usuarios:
        senha = input("Digite a sua senha de 5 dígitos: ")
        if biblioteca.usuarios[nome].senha == senha:
            titulo = input("Digite o título do livro que deseja descadastrar: ")
            if titulo in biblioteca.livros:
                sugestao_genero = input("Você deseja sugestões de gênero? (S/N): ").lower()
                if sugestao_genero in ("s", "sim"):
                    print("Sugestões de gênero disponíveis:\n", generos)
                    genero = input("Digite o gênero do livro: ")
                else:
                    genero = input("Digite o gênero do livro: ")

                for i in range(5):
                    senha_admin = input("Digite a senha do administrador: ")
                    if senha_admin == admsenha:
                        del biblioteca.livros[titulo]
                        print("Livro descadastrado com sucesso!")
                        return
                    else:
                        print("A senha do administrador está incorreta, tente novamente:")
                print("Número máximo de tentativas atingido. Retornando ao menu principal.")
            else:
                print("O livro não foi encontrado em nosso cadastro.")
        else:
            print("Tem algo errado com a sua senha, tente novamente:")
    else:
        print("Você não foi encontrado em nosso cadastro.")

# Função para consultar livro
def consultar_livro():
    
    opcao = input("Escolha uma opção de consulta:\n\n1. Por Título\n\n2. Por Autor\n\n3. Por Gênero\n\n4. Todos os Livros\n\n5. Voltar ao menu anterior\n\nDigite o número da opção desejada: ")
    if opcao == '1':
        titulo = input("\nDigite o título do livro: ")
        for livro in biblioteca.livros.values():
            if livro.titulo.lower().startswith(titulo.lower()):
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')
                if livro.quantidade > 0:
                    print("Este livro está disponível!")
                else:
                    print("Este livro não está disponível no momento.")
    elif opcao == '2':
        autor = input("\n1Digite o nome do autor: ")
        for livro in biblioteca.livros.values():
            if livro.autor.lower().startswith(autor.lower()):
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')
                if livro.quantidade > 0:
                    print("Este livro está disponível!")
                else:
                    print("Este livro não está disponível no momento.")
    elif opcao == '3':
        genero = input("Digite o gênero do livro: ")
        genero = encontrar_genero(genero)
        for livro in biblioteca.livros.values():
            if livro.genero.lower() == genero.lower():
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')
                if livro.quantidade > 0:
                    print("Este livro está disponível!")
                else:
                    print("Este livro não está disponível no momento.")
    elif opcao == '4':
        for livro in biblioteca.livros.values():
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')
            if livro.quantidade > 0:
                print("Este livro está disponível!")
            else:
                print("Este livro não está disponível no momento.")



# Função principal
def main():
    
    while True:
        print('  ')
        print("Bem-vindo a Matchlivros, a sua Biblioteca!")
        print ("_____________________________________________\n")
        print("1. Criar uma conta\n")
        print("2. Fazer login\n")
        print("3. Encerrar minha conta\n")
        print("4. Sair\n")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            if login():
                while True:
                    print("  ")
                    print("Biblioteca\n")
                    print("1. Cadastrar ou doar livros\n")
                    print("2. Consultar livro que temos\n")
                    print("3. Descadastrar um  livro\n")
                    print("4. Sair\n")
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                        cadastrar_livro()
                    elif opcao == '2':
                        consultar_livro()
                    elif opcao == '3':
                        descadastrar_livro()
                    elif opcao == '4':
                        break
            else:
                print("O login falhou.")
        elif opcao == '3':
            descadastrar_usuario()
        elif opcao == '4':
            break

 # Executando a função principal
if __name__ == "__main__":
    while True:
        main()