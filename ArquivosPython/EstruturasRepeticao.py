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

