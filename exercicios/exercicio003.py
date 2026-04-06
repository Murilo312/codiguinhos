numeral = True    
while numeral == True:
    try:
        numero1 = int(input('fala um numero ai neguinho '))
        numero2 = int(input('fala outro número se tu tem aura '))
        resultado = numero1 + numero2
        print (f'ei tu sabia que se somar eles vai dar {resultado}')
        numeral = False
    except:
        print ('falei pra dizer um numero neguinho')
        print ('tente novamente')