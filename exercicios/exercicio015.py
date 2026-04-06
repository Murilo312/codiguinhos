erro = True
while erro == True:
    try:
        dias = int(input('por quantos dias voce alugou o carro? '))
        km = float(input('por quantos km voce rodou? '))
        dinheiro = (dias * 60) + (km * 0.15)
        print (f'já que voce usou o carro por {dias} dias e por {km}km entao você deve pagar {dinheiro} reais')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
         