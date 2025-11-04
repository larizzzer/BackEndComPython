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

#IF aninhado
conta_normal = False
conta_universitaria = False
conta_especial = True
saldo = 2000
saque = 1600
cheque_especial = 450
   
if conta_normal:

    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com o cheque especial!')
    else:
        print('Não é possível realizar o saque, saldo insuficiente!')

elif conta_universitaria:

    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')

elif conta_especial:
    print('Conta especial selecionada!')

else:
    print('Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!')

#IF ternário
saldo = 2000
saque = 3000

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')