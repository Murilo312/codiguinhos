numero = True
while numero == True:
    try:
        n=int(input("tabuada do: "))
        final=int(input('voce deseja saber até qual número da tabuada? '))
        x=1
        print ('----------------')
        while x<=final:
            print(n, 'x', x, '=',n*x)
            x= x+1
        numero = False
        print ('----------------')
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')