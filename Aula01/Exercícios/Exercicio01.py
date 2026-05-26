'''
Exercício 1

Crie uma função chamada calcular_media() que:

Receba duas notas.
Retorne a média.

Ao terminar No controle de Versão: Commit & Push

'''
# Criar a função
def calcular_media(nota1, nota2):
    media = (int(nota1) + int(nota2)) / 2 #Casting
    return media


n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")

print(calcular_media(n1, n2))
