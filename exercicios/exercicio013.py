erro = True
while erro == True:
    try:
        salario = float(input('quantos reais o cara recebia de salario? '))
        salarionovo = salario + salario/10
        print (f'sabia que esse cara que tinha o salário de {salario} passou a ter o salario de {salarionovo} depois do aumento de 10%')
        erro = False
    except:
        print ('o valor precisa ser um número')
        print ('tente novamente')
        