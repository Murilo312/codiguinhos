import random
a1 = input('primeira pessoa: ')
a2 = input('primeira pessoa: ')
a3 = input('primeira pessoa: ')
a4 = input('primeira pessoa: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print (f'a pessoa escolhida foi {escolhido}')