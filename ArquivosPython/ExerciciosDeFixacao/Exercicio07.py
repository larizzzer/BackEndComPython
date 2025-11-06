#Constante e cálculo de desconto

DESCONTO = 0.1

preco = float(input('Digite o preço do produto: '))

valor_do_desconto = preco * DESCONTO
preco_com_desconto = preco - valor_do_desconto

print(f'O valor do preço com desconto fica: {preco_com_desconto:.2f}')