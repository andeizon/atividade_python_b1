r1 = input('telefonou para a vitima?')
r2 = input('esteve no local do crime?')
r3 = input('mora perto da vítima?')
r4 = input('devia para a vítima?')
r5 = input('já trabalhou com a vítima')

acumulador = 0
if r1 == "sim":
    acumulador=acumulador + 1

if r2 == "sim":
    acumulador=acumulador + 1

if r3 == "sim":
    acumulador=acumulador +1

if r4 == "sim":
    acumulador=acumulador +1

if r5 == "sim":
    acumulador=acumulador +1

if acumulador == 0 or acumulador == 1:
    print('inocente')
if acumulador == 2:
    print('suspeita')
if acumulador ==3 or acumulador == 4:
    print('cúplice')
if acumulador ==5:
    print('assassino')
