erro = True
while erro == True:
    try:
        ca = float (input ('quanto mede o cateto adjacente? '))
        co = float (input ('quanto mede o cateto oposto? '))
        h2 = ca**2 + co**2
        h = h2**0.5
        print (f'a hipotenusa deste triangulo retangulo vai ser {h:.2f}')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
        