# verificação de vogal

letra = input('Digite qualquer letra: ').upper()
VOGAIS = 'AEIOU'

if letra in VOGAIS:
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante!')