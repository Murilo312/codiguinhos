rodar = True
media = 0
while rodar == True:
    try:
        a = float(input('fala sua primeira nota ai '))
        b = float(input('fala ai tua segunda nota '))
        if (a >=0 and a<=10) and (b>= 0 and b<= 10):
            media = (a + b)/2
            if media >= 7:
                print (f'sua media final foi {media:.2f} e você está PASSADO DE ANO')
                rodar = False
            else:
                media = (a + b)/2
                print (f'sua media final foi {media:.2f} e voê está REPROVADO DE ANO')
                rodar = False
        else:
            print ('voce não pode tirar essa nota')
            print ('tente novamente')
    except:
        print ('tua nota tem que ser um número')
        print ('tente novamente')
