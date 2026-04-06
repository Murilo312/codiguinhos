numero = False
while numero == False:
    try:
        numero = int(input('fala um número '))
        dobro = numero * 2
        triplo = numero * 3
        raiz = numero **0.5
        print (f'o dobro desse número é {dobro}')
        print (f'o triplo desse numero é {triplo}')
        print (f'a raiz quadrada desse numero é {raiz:.2f}')
        numero = True
    except:
        print ('eu falei pra falar um numero neguinho')
        print ('tente novamente')