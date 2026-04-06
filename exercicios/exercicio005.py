numero = False
while numero == False:    
    try:
        n = int (input ('fale um número inteiro'))
        antecessor = 0
        sucessor = 0
        antecessor = n-1
        sucessor = n + 1
        print (f'analisando sua resposta eu confirmo que o antecessor de {n} é {antecessor} e o sucessor de {n} é {sucessor}')
        numero = True
    except:
        print ('eu falei pra tu dizer um numero inteiro neguinho')
        print ('tente novamente')