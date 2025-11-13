nome = 'Larissa'
idade = 23
profissao = 'Engenheira de Dados'
linguagem = 'Python'
saldo =45.435

dados = {'nome': 'Larissa', 'idade': 28}

print('Nome: %s Idade: %d' % (nome, idade)) # --> Estilo antigo e não há mais utilização

print('Nome: {} Idade: {}'.format(nome, idade)) # --> Método Format mais verboso de se escrever

print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {1} Idade: {0} Nome: {1} {1}'.format(idade, nome))

print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))
print('Nome: {name} Idade: {age}'.format(name=nome, age=idade))
print('Nome: {nome} Idade: {idade}'.format(**dados)) # --> Pega as variáveis de um dicionário

print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}') #Saldo com 10 de tamanho e arredondado com 2 casas decimais
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}')
