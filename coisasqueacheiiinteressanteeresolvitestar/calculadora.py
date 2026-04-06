print ('----------------')
print ('   CALCULADORA')
print ('----------------')
erro = True
while erro == True:
    try:
        operação = input ('qual operação voce quer fazer? ')
        if operação == 'multiplicação' or operação == 'multiplicacao':
            n1 = int(input('qual o primeiro número? '))
            n2 = int(input('qual o segundo número? '))
            resultado = n1 * n2
            print (f'o resultado da multiplicação entre {n1} e {n2} é igual a {resultado}')
            erro = False
        elif operação == 'divisão' or operação == 'divisao':
            n1 = int(input('qual o primeiro número? '))
            n2 = int(input('qual o segundo número? '))
            resultado = n1 / n2
            print (f'o resultado da divisão entre {n1} e {n2} é igual a {resultado}')
            erro = False
        elif operação == 'adição' or operação == 'adicao' or operação == 'soma':
            n1 = int(input('qual o primeiro número? '))
            n2 = int(input('qual o segundo número? '))
            resultado = n1 + n2
            print (f'o resultado da soma entre {n1} e {n2} é igual a {resultado}')
            erro = False
        elif operação == 'subtração' or operação == 'subtracao':
            n1 = int(input('qual o primeiro número? '))
            n2 = int(input('qual o segundo número? '))
            resultado = n1 - n2
            print (f'A diferença entre {n1} e {n2} é igual a {resultado}')
            erro = False
        elif operação == 'potenciação' or operação == 'potenciacao':
            n1 = int(input('qual a base? '))
            n2 = int(input('qual a potencia? '))
            resultado = n1 ** n2
            print (f'o resultado de {n1} elevado a {n2} é igual a {resultado}')
            erro = False
        elif operação == 'radiciação' or operação == 'radiciacao':
            n1 = int(input('qual o número? '))
            n2 = int(input('qual o indice do radical? '))
            resultado = n1 ** (1/n2)
            print (f'a raiz do numero {n1} no indice {n2} é igual a {resultado}')
            erro = False
        else:
            print ('operação não encontrada')
            erro = True
    except:
        print ('erro encontrado')
        print ('tente novamente')