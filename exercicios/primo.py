numero = int(input ('fala um número ai '))
contador = 2
if numero < 2 and numero >= 0:
    print ('esse numero não é primo')
elif numero < 0:
    print ('esse numero e negativo')
elif numero == 2:
    print ('esse numero e primo')
else:
    while contador <= numero:
        if numero %contador == 0:
            print (f'esse numero nao e primo, ele é divisível por {contador}')
            break
        contador = contador + 1
        if contador == numero:
            print ('esse numero e primo')
            break