erro = True
while erro == True:
    try:
        preco = float(input('quantos reais estava a camisa da loja? '))
        desconto = preco - preco/10
        print (f'sabia que essa camisa de {preco} reais está a {desconto} reais depois do desconto de 10%')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
        