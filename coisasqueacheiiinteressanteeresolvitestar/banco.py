print ('-----------------------')
print ('BANCO DIGITAL DO MURILO')
print ('-----------------------')
deposito = 0.0
saldo = 0.0
sair = False
retirada = 0.0
desejo = ''
quantitade_erro = 0
erros = []
erro = False
while sair == False:   
    desejo = str(input('O que deseja fazer? depositar dinheiro, retirar dinheiro ou sair do banco? '))
    if desejo == 'retirar dinheiro' or desejo == 'retirar':
        try:
            retirada = float(input('quanto deseja retirar '))
        except Exception as e:
             print('ei bixin fez merda')
             retirada = 0
             erro = True
             quantitade_erro = quantitade_erro + 1
             erros.append(e)
        if retirada < 0:
            print ('voce nao pode retirar uma quantia de dinheiro negativa')
            quantitade_erro = quantitade_erro + 1
            erros.append ('retirar uma quantia negativa de dinheiro')
            erro = True
        elif retirada > saldo:
            print (f'nao pode retirar esse dinheiro, voce tem apenas {saldo} de saldo')
            quantitade_erro = quantitade_erro + 1
            erros.append('retirar mais do que tem de saldo')
            erro = True
        else:
            saldo = saldo - retirada
            print (f'agora seu saldo é {saldo}')
    elif desejo == 'depositar' or desejo == 'depositar dinheiro' :
        try:
            deposito = float(input('quanto voce deseja depositar? '))
        except Exception as e:
            print ('ei bixin fez merda')
            deposito = 0
            erro = True
            quantitade_erro = quantitade_erro + 1
            erros.append(e)
        if deposito < 0:
            print ('voce nao pode depositar uma quantia negativa')
            quantitade_erro = quantitade_erro + 1
            erros.append('depositar uma quantia de dinheiro negativa')
            erro = True
        elif deposito >= 0:
            saldo = saldo + deposito
            print ('seu saldo atual é', saldo)
    elif desejo == 'sair' or desejo == 'sair do banco':
        print ("SAINDO ...")
        sair = True
    else:
        print('comando não encontrado')
        print ('tente novamente')
        quantitade_erro = quantitade_erro + 1
        erros.append('comando não encontrado')
        erro = True
if erro == True:
    if quantitade_erro == 1:
        print (f'o usuario provocou um erro {quantitade_erro} vez')
    else:
        print (f'o usuario provocou um erro {quantitade_erro} vezes')
    print ('os erros foram: ')
    for er in erros:
        print (er)
