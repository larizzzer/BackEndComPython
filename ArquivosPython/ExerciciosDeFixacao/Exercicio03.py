#Percorre os números de 1 a 10 e pula os números pares

for numero in range(1, 11):
    
    if numero % 2 == 0:
        continue

    print(numero)

