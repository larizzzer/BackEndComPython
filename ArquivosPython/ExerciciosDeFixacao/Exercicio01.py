#Saudação condicional: user digita o nome e em seguida aparece 'Olá nome, Bem-vinda!'

nome = input('Digite o seu nome: ')

if nome == 'Ana':
    print('Olá, Ana! Bem-vinda!')
else:
    print(f'Olá, {nome}!')