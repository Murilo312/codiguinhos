import math
erro = True
while erro == True:
    try:
        angulo = float(input('qual angulo voce quer? '))
        seno = math.sin(math.radians(angulo))
        cosseno = math.cos(math.radians(angulo))
        tangente = math.tan(math.radians(angulo))
        print (f'o seno do angulo de {angulo} graus equivale a {seno:.2f}')
        print (f'o cosseno do angulo de {angulo} graus equivale a {cosseno:.2f}')
        print (f'a tangente do angulo de {angulo} graus equivale a {tangente:.2f}')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')