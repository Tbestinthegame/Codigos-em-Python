cont = 0
while cont != 1:
    n1 = int(input('Digite um valor:'))
    n2 = int(input('Digite outro valor:'))

    if n1 > n2:
        print('O primeiro valor é maior.')

    elif n2 > n1:
        print('O segundo valor é o maior.')

    else:
        print('Não tem valor maior, ambos são iguais.')
        
    cont = int(input('Deseja continuar o programa? 0 para sim e 1 para não '))