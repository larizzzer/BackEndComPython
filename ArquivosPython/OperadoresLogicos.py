#O operador lógico tem que ser usado em conjunto com o operador de comparação
print(True and True and True) #AND = retorna TRUE se ambos forem TRUE
print(True and False and True)
print(False and False and False)
print(True or True or True)  #OR = retorna TRUE se pelo menos uma das expressões forem TRUE
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite  #uma quebra de expressão para não se usar uma expressão muito grande
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque #para tornar o código mais legível

expressao3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao3)
