texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto: #percorre letra a letra verificando quais são as vogais e mostra elas
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: #não é muito comum utilizar ele no dia a dia
    print('\n') # adiciona uma quebra de linha


#range --> produz sequências númericas, sendo seu ínicio inclusivo e seu final exclusivo, mosta 90, não 91 e conta de 9 em 9
for numero in range(0, 91, 9): 
    print(numero)


opcao = -1

while opcao != 0: #executa várias e várias vezes sem um número limite até você digitar 0
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if opcao == 1:
        print('Sacando o dinheiro....')
    elif opcao == 2:
        print('Imprimindo o extrato da sua conta bancária...')
else: #não é muito utilizado, assim como no for
    print('Obrigado por usar nosso sistema bancário, até logo!')


numero = -1

while True: 
    numero = int(input('Informe um número: '))

    if numero == 10:
        break #para o programa caso o 10 seja digitado

    print(numero)