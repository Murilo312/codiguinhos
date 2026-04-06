erro = True
while erro == True:
    try:
        a=float(input('ei bixin fala um número decimal ai' ))
        a = a//1
        print (f'o valor inteiro é {a}')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
        