print(int(1.984564)) #não importa o número de casas, sempre trás o valor 1

print(int('10'))

print(float('10.10')) #ignora o 0 pois, 10.1 e 10.10 é a mesma coisa

print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

dinheiro = 522.12
dinheiro_str = str(dinheiro)
print(type(dinheiro))
print(type(dinheiro_str))

print(100 / 2) #transforma em FLOAT
print(100 // 2) #resulta em uma divisão inteira

#type() mostra qual é o tipo da variável --> print(type(str(10.10))) 