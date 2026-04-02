contador1 = 0
pontos = [0.5, 0.5, 0.5, 0.5, 0.5]
valido = True
while contador1 < 5:
    contador2 = contador1 + 1
    pontos[contador1] = float(input(f'fala ai a tua {contador2}o nota '))
    if pontos[contador1] > 10 or pontos[contador1] < 0:
        print (f'ei mocinho ta de brincadeira comigo?, o numero {pontos[contador1]} é invalido e impossivel tu tirar essa nota seu but')
        valido = False
        break
    contador1 = contador1 + 1
media = (pontos[0] + pontos[1] + pontos[2] + pontos[3] + pontos[4]) /5
if valido == True:
    print (f'a media entre os numeros {pontos} eh igual a {media}')