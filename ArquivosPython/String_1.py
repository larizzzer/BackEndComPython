nome = 'LaRIsSa'

print(nome.upper()) # --> Tudo MAIÚSCULO
print(nome.lower()) # --> Tudo minúsculo
print(nome.title()) # --> Deixa a primeira letra Maiúscula

texto = '   Hello World!     '

print(texto)
print(texto.strip())  # --> Remove todos os espaçoes
print(texto.lstrip()) # --> Remove os espaços da esquerda
print(texto.rstrip()) # --> Remove os espaços da direita

curso = 'Python'

print(curso.center(14, '#')) # --> Centraliza o texto da variável e coloca # nos espaços em branco
print('-'.join(curso)) # --> Junta os - com o texto da variável