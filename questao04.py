l1 = int(input('informe um número'))
l2 = int(input('infor outro número'))
l3 = int(input('informe um outro número'))

if  (l1 + l2 > l3) and (l3 + l2 > l1) and (l1 + l3 > l2):
    print('é um triângulo')
    if l1 == l2 == l3:
        print('é um triângulo equilátero')
    elif (l1 == l2 != l3) or (l2 == l3 != l1) or (l1 == l3 != l2):
        print('é um triângulo isósceles')
    elif l1 != l3 != l2:
        print('é um triângulo escaleno')
else:
    print('não é um triângulo')
