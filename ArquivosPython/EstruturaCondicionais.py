MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

#if simples, se é verdade executa o bloco
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CNH.')


if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
else: #se caso a condição for FALSE, executa o else
    print('Ainda não pode tirar a CNH.')

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
elif idade == IDADE_ESPECIAL: #há um teste e se caso retorna TRUE, o bloco dentro do elif é executado
    print('Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas!')
else:
    print('Ainda não pode tirar a CNH.')