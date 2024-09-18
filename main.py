import os
import random


# Classes


class Usuario():
    def __init__(self, cpf, codigo, nome, curso):
        self.cpf = cpf
        self.codigo = codigo
        self.nome = nome
        self.curso = curso
        self.fichasAlmoco = 0
        self.fichasJanta = 0
        


# Funções


def listar_usuarios():
    print("_________LISTA DE USUARIOS_________")
    print(' ')
    if not usuarios:
        limpe()
        print('Lista vazia')
    for cpf, usuario in usuarios.items():
        print(f'CPF: {cpf}')
        print(f'Código: {usuario.codigo}')
        print(f'Nome: {usuario.nome}')
        print(f'Curso: {usuario.curso}')
        print(f'Fichas disponíveis para almoco: {usuario.fichasAlmoco}')
        print(f'Fichas disponíveis para janta: {usuario.fichasJanta}')
        print('')

# CADASTRAR USUÁRIO


print('Obrigado!')


import random

def cadastrar_usuario():
    print("_________CADASTRO DE USUARIO_________")
    print('')
    print('Informe os 11 números do CPF!')
    print('EXEMPLO: 13507973604')

    while True:
        cpf = input('Entre o CPF: ')
        limpe()
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido! Certifique-se de que contém apenas 11 números.")

    limpe()

    if cpf in usuarios:
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

        while True:
            print('Formato nome: JOSE XXXXXX DA XXXXX SILVA')
            nome = input('Entre o nome completo: ')
            limpe()
            if all(c.isalpha() or c.isspace() for c in nome) and len(nome.split()) > 1:  # Verifica se é apenas letras e espaços
                break
            else:
                print("Nome inválido! Por favor, insira um nome válido sem números ou caracteres especiais.")

        while True:
            print('Formato curso: BSI = Bacharelado em Sistemas da Informação')
            curso = input('Entre o curso: ')
            limpe()
            if all(c.isalpha() or c.isspace() for c in curso) and len(curso.split()) > 1:  # Verifica se é apenas letras e espaços
                break
            else:
                print("Curso inválido! Por favor, insira um curso válido sem abreviações ou caracteres especiais")

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
    print('_________COMPRAR FICHA________')
    cpf = input('Entre o CPF do usuário: ')
    limpe()
    if cpf in usuarios:
        while True:
            try:
                quantidade = int(input('Quantas fichas deseja comprar? '))
                limpe()
                if 1 <= quantidade <= 100:
                    break
                else:
                    print("Quantidade inválida! Deve ser entre 1 e 100. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")
        
        # Escolha de refeição
        print('Entre a opção: ALMOÇO [1]   JANTAR [2]  VOLTAR [0]')
        op = input()
        limpe()
        
        if op == '1':
            preco = 3.50
            ficha_bonus = quantidade // 5  # 1 ficha grátis a cada 5 almoços
            usuarios[cpf].fichasAlmoco += quantidade + ficha_bonus
        elif op == '2':
            preco = 3.00
            ficha_bonus = quantidade // 7  # 1 ficha grátis a cada 7 jantas
            usuarios[cpf].fichasJanta += quantidade + ficha_bonus
        elif op == '0':
            return  # Retorna ao menu anterior ou encerra
        else:
            print('Entre um valor válido!')
            return
        
        # Cálculo e exibição do pagamento apenas para as fichas pagas
        print('==============================')
        total_a_pagar = quantidade * preco  # Não inclui as fichas bônus
        print(f'Pagamento total: {quantidade} * R$ {preco:.2f}')
        print(f'TOTAL A SER PAGO: R$ {total_a_pagar:.2f}')
        print('==============================')
        if ficha_bonus > 0:
            print(f"Parabéns! Você ganhou {ficha_bonus} ficha(s) bônus!")
        print(f'Ficha(s) comprada(s) com sucesso para {usuarios[cpf].nome}!')
        print(f'Agora {usuarios[cpf].nome} possui {usuarios[cpf].fichasAlmoco} almoco(s) e {usuarios[cpf].fichasJanta} janta(s).')
        
        while True:
            print('ENCERRAR [0]      Menu principal [1]')
            op = input()
            if op == '0':
                encerrar()
            elif op == '1':
                limpe()
                menu_principal()
            else:
                print('Entre um valor válido!')
    else:
        print('Usuário não encontrado')

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

#atualizar cadastro

def atualizar_cadastro():
    print('________ATUALIZAR CADASTRO________')
    while True:
        cpf = input('Entre o CPF: ')
        limpe()
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido! Certifique-se de que contém apenas 11 números.")

    if cpf in usuarios:
        print(f'Usuário encontrado: {usuarios[cpf].nome}')
        aviso = (
            "****************************************\n"
        "*              AVISO!                 *\n"
        "*  Por questões de segurança, apenas  *\n"
        "*  o nome e o curso do usuário podem   *\n"
        "*  ser atualizados. Para realizar outras *\n"
        "*  alterações, recomenda-se deletar o   *\n"
        "*  usuário e cadastrar um novo com as   *\n"
        "*  informações atualizadas.             *\n"
        "****************************************"
        )
        print(aviso) 
        while True:
            print('Formato nome: JOSE XXXXXX DA XXXXX SILVA')
            nome = input('Entre o novo nome de usuário: ')
            limpe()
            if all(c.isalpha() or c.isspace() for c in nome) and len(nome.split()) > 1:  # Verifica se é apenas letras e espaços
                break
            else:
                print("Nome inválido! Por favor, insira um nome válido sem números ou caracteres especiais.")
        while True:
            print('Formato curso: BSI = Bacharelado em Sistemas da Informação')
            curso = input('Entre o novo curso: ')
            limpe()
            if all(c.isalpha() or c.isspace() for c in curso) and len(curso.split()) > 1:  # Verifica se é apenas letras e espaços
                break
            else:
                print("Curso inválido! Por favor, insira um curso válido sem abreviações ou caracteres especiais")

        confirmacao = input('Tem certeza que deseja alterar estas informações de usuário? (s/n): ').lower()
        
        if confirmacao == 's':
            usuarios[cpf].nome = nome 
            usuarios[cpf].curso = curso 
            print('Update realizado com sucesso!')
        elif confirmacao == 'n':
            print('Update cancelado.')
        else:
            print('Entrada inválida! Deleção cancelada.')
    else:
        print('Usuário não encontrado.')

    input('Tecle [ENTER] para continuar...')
    limpe()

#deletar usuário
def deletar_usuario():
    print("_________DELETAR USUÁRIO_________")
    
    while True:
        cpf = input('Entre o CPF: ')
        limpe()
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido! Certifique-se de que contém apenas 11 números.")

    if cpf in usuarios:
        print(f'Usuário encontrado: {usuarios[cpf].nome}')
        confirmacao = input('Tem certeza que deseja deletar este usuário? (s/n): ').lower()
        
        if confirmacao == 's':
            del usuarios[cpf]
            print('Usuário deletado com sucesso!')
        elif confirmacao == 'n':
            print('Deleção cancelada.')
        else:
            print('Entrada inválida! Deleção cancelada.')
    else:
        print('Usuário não encontrado.')

    input('Tecle [ENTER] para continuar...')
    limpe()


# menu principal

def menu_principal():
    while True:
        print("_____________BEM VINDO___________")
        print('')
        print('LISTAR USUÁRIOS    [1]')
        print('CADASTRAR USUÁRIO  [2]')
        print('COMPRAR FICHA      [3]')
        print('DELETAR USUÁRIO    [4]')
        print('ATUALIZAR CADASTRO [5]')
        print('SAIR               [0]')
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
        elif op == '4':
            deletar_usuario()
        elif op == '5':
            atualizar_cadastro()
        else:
            print('Informe um valor válido!')
            input('Tecle [ENTER]')
            limpe()


menu_principal()