print ('-----------------------')
print ('BANCO DIGITAL DO MURILO')
print ('-----------------------')
deposito = 0.0
saldo = 0.0
sair = False
retirada = 0.0
desejo = ''

while sair == False:   
    desejo = str(input('O que deseja fazer? depositar dinheiro, retirar dinheiro ou sair do banco? '))
    if desejo == 'retirar dinheiro' or desejo == 'retirar':
        retirada = float(input('quanto deseja retirar '))
        if retirada < 0:
            print ('voce nao pode retirar uma quantia de dinheiro negativa')
        elif retirada > saldo:
            print (f'nao pode retirar esse dinheiro, voce tem apenas {saldo} de saldo')
        else:
            saldo = saldo - retirada
            print (f'agora seu saldo é {saldo}')
    elif desejo == 'depositar' or desejo == 'depositar dinheiro' :
        deposito = float(input('quanto voce deseja depositar? '))
        if deposito < 0:
            print ('voce nao pode depositar uma quantia negativa')
        else:
            saldo = saldo + deposito
            print ('seu saldo atual é', saldo)
    elif desejo == 'sair' or desejo == 'sair do banco':
        print ("SAINDO ...")
        sair = True
    else:
        print('comando não encontrado')
        print ('tente novamente')
