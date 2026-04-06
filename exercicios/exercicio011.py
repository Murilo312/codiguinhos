erro = True
while erro == True:
    try:
        largura = float(input('qual a largura da parede ? '))
        altura = float(input('qual a altura da parede? '))
        area = largura * altura
        tinta = area/2
        print (f'uma parede {largura}m x {altura}m tem {area}m² de área')
        print (f'para pintar uma parede de {area}m² de área é necessario {tinta:.2f}L de tinta')
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')