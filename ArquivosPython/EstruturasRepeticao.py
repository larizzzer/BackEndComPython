texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto: #percorre letra a letra verificando quais são as vogais e mostra elas
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: #não é muito comum utilizar ele no dia a dia
    print('\n') # adiciona uma quebra de linha

