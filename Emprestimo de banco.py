print('Banco do Brasil >>>>>>>')
print('Obrigado por fazer um emprestimo com a gente!')
casa = float(input('Digite o valor da casa que você deseja:'))
salario = float(input('Agora digite seu salario:'))
anos = float(input('Pra finalizar, digite em quantos anos você pretende pagar a casa:'))
anual = casa/anos
mensal = anual / 12
negaçao_se = (salario * 0.3) + salario
sub = salario - mensal
if sub < 0:
    sub = sub * (-1)
print(f'Por ano você pagará {anual}')
print('A mensalidade por mês será de {0:3.2f}'.format(mensal))
print('A subtração da mensalidade com seu salario é de {0:3.2f}'.format(sub))
print('Valor máximo que aprestação mensal pode ir para que o emprestimo seja aceito: {0:3.2f}'.format(negaçao_se))

if mensal > salario and mensal > negaçao_se:
    print('Lamento , mas a prestação supera 30%, por isso não é possivel realizar o emprestimo.')
else:
    print('Parabens, o emprestimo foi aceito!')