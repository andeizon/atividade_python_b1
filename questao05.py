calculadora = input('escolha a operação: A= adição, S= subtração, D= divisão, M= Multiplicão')
z = int(input('digite um  número:'))
k = int(input('digite um número:'))

if calculadora =='A':
    print(z + k)
if calculadora == 'S':
    print(z - k)


if calculadora == 'M':
    print(z * k)
if calculadora == 'D':
    if  k != 0:
        print(z / k)

    if  k == 0:
        print('error')


