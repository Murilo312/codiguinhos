print ('----------------------')
print ('SEQUENCIA DE FIBONACCI')
print ('----------------------')
print('')
quantitade = int(input('quantos números da sequência de fibonnaci você quer? '))
repetição = 1
numero1 = 0
numero2 = 0
numero3 = 0
while repetição < quantitade + 1:
    if repetição %3 == 1:
        numero1 = numero2 + numero3
        print (f'o {repetição}º número é {numero1}')
    elif repetição %3 == 2:
        if numero2 == 0:
            numero1 = 1
        numero2 = numero1 + numero3
        print (f'o {repetição}º número é {numero2}')
    else:
        if numero1 == 1:
            numero1 = 0
        numero3 = numero1 + numero2
        print (f'o {repetição}º número é {numero3}')
    repetição = repetição + 1
