# Exercício 01
'''
Crie um programa que:
    1. Receba nome e idade.
    2. Exiba mensagem personalizada.
'''

# Criar a função
def mostrar_mensagem(nome, idade):
    return f"Olá, {nome}, você tem {idade} anos!"


# Criar as variáveis
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Chamar a função
print(mostrar_mensagem(nome, idade))
