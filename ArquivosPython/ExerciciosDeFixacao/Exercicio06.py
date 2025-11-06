# Menu simples com o while

while True:
    opcao = int(input(' 1. Opção A\n 2. Opção B\n 3. Sair\n Escolha uma opção: '))

    if opcao == 1:
        print('Você escolheu A\n')
    elif opcao == 2:
        print('Você escolheu B\n')
    elif opcao == 3:
        break
    else:
        print('Opção inválida\n')