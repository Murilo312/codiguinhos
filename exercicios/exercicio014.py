erro = True
while erro == True:
    try:
        celsius = float(input('fale a temperatura em graus celsius '))
        f = (celsius*(9/5) + 32)
        print (f'a temperatura {celsius}C equivale a {f}F')
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
        