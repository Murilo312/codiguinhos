rodar = True
while rodar == True:
    try:
       real = float(input('quantos reais você tem na sua conta bancaria? '))
       dolar = real/5.16
       print (f'com {real:.2f} reais você pode converter para {dolar:.2f} dólares')
       rodar = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')