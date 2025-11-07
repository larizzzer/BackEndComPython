# Mostrar uma tabuada exibindo 6x1 = 5 6x2 = 12

numero = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range(1, 11):
    print(f'{numero} x {tabuada} = {numero * tabuada}')