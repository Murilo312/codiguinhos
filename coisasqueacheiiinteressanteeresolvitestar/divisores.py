print ('----------------')
print ('   DIVISORES')
print ('----------------')
erro = True
while erro == True:
    try:
        numero = int(input('fala um número ai '))
        numero = numero // 1
        divisores = 0
        cont = 1
        if numero <= 0:
            print ('esse numero nao tem divisores')
        else:
            while cont <= numero:
                if numero %cont == 0:
                    divisores = divisores +1
                    print (f'o {divisores}o divisor do numero {numero} é {cont}')
                cont = cont + 1
            if divisores == 2:
                print ('esse número é primo, ele possui apenas dois divisores')
            elif divisores == 1:
                print ('esse número só tem um divisor')
            else:
                print (f'o numero {numero} tem {divisores} divisores')
            erro = False
    except:
        print ('NÚMERO INVÁLIDO')