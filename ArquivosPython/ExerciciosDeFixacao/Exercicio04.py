# User digita um número e soma todos eles até o usuário digitar 0
soma = 0

while True:
    numero = int(input('Digite um número inteiro: '))

    if numero > 0:
        soma += numero
    elif numero == 0:
        print(soma)
        break