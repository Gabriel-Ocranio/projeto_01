import os
import random


# Classes


class Usuario():
    def __init__(self, cpf, codigo, nome, curso):
        self.cpf = cpf
        self.codigo = codigo
        self.nome = nome
        self.curso = curso


# Funções


# LOGIN (usuário já cadastrado)
def login():
    cod = int(('Código: '))
    print(cod in usuarios[cod])


def listar_usuarios():
    print("_________LISTA DE USUÁRIOS_________")
    print(' ')
    for cpf, usuario in usuarios.items():
        print(f'CPF: {cpf}')
        print(f'Código: {usuario.codigo}')
        print(f'Nome: {usuario.nome}')
        print(f'Curso: {usuario.curso}')
        print('')

# CADASTRAR USUÁRIO


def cadastrar_usuario():
    print("_________CADASTRO DE USUÁRIO_________")
    print('')
    cpf = input('Entre o CPF: ')

    if cpf in usuarios:
        limpe()
        print('CPF já cadastrado!')
        while True:
            entrada = input('VOLTAR [ENTER]   ENCERRAR [0]')
            if entrada == '':
                return cadastrar_usuario()
            elif entrada == '0':
                return encerrar()
            else:
                print('Entre um valor válido')

    else:
        codigo = random.randint(10000, 99999)
        nome = input('Entre o nome completo: ')
        curso = input('Entre o curso: ')
        limpe()
        print('____CONFIRME OS DADOS____')
        print('')
        print('CPF: ', cpf)
        print('Nome: ', nome)
        print('Curso: ', curso)

    print('Para confirmar, tecle [ENTER]')
    print('Voltar               [0]')
    op = input()
    limpe()

    if op == '0':
        limpe()
        return cadastrar_usuario()

    elif op == '':
        novo_usuario = Usuario(cpf, codigo, nome, curso)
        usuarios[cpf] = novo_usuario
        limpe()
        print('USUÁRIO CADASTRADO COM SUCESSO')
        return menu_principal()


# Comprar a ficha
def comprar_ficha():
    print('Comprar ficha')


# Limpar a tela
def limpe():
    os.system('cls' if os.name == 'nt' else 'clear')


# Funções utilitárias


def encerrar():
    limpe()
    print('Programa encerrado!')
    exit()


# Variável global para armazenar os usuários
usuarios = {}

# menu principal


def menu_principal():
    while True:
        print("_____________BEM VINDO___________")
        print('')
        print('LISTAR USUÁRIOS   [1]')
        print('CADASTRAR USUÁRIO [2]')
        print('COMPRAR FICHA     [3]')
        print('SAIR              [0]')
        op = input('Entre a opção: ')
        limpe()
        if op == '0':
            return encerrar()
        elif op == '1':
            listar_usuarios()
        elif op == '2':
            cadastrar_usuario()
        elif op == '3':
            comprar_ficha()
        else:
            print('Informe um valor válido!')
            input('Tecle [ENTER]')
            limpe()


menu_principal()
