def sacar(valor): #identação
    saldo = 500 #tudo que estiver a 4 espaços faz parte da função(sacar)

    if saldo >= valor: 
        print('Valor sacado!') #tudo que estiver a 8 espaços está dentro do IF e do ELSE
        print('Retire o seu dinheiro na boca do caixa!\n')
    else:
        print('Você não possui saldo!')
        print('Reveja seu saldo e tente novamente!\n')
    
    print('Obrigado por ser nosso cliente, tenha um bom dia!\n') #Está dentro da função(sacar)

def depositar(valor):
    saldo = 500 #se estiver sem identação, o vscode indicará o erro!
    saldo += valor

    print('Saldo depositado!')
    print(f'Seu novo saldo é {saldo}!')

        

depositar(300)
sacar(1200)