nome = input('Digite seu nome: ') # pega dados digitados
idade = input('Digite sua idade: ')

print(nome, idade) # mostra os dados digitados
print('Teste', end=' ')
print(nome, idade, end='...\n') # o end por padrão possui o \n
print(nome, idade, sep='#',end='...\n') 
print(nome, idade, sep='#') # o sep por padrão é um espaço

