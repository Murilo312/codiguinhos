import os
vitoriaX = False
vitoriaO = False
c = 0
jogadas = [1,2,3,4,5,6,7,8,9]
print ('---------------------')
print ('   JOGO DA VELHA')
print ('---------------------')
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
def mostrar_tabuleiro():
    c = 0
    for jogo in jogadas:
        c = c+1
        if c%3 == 1:
            print()
            print(jogo, end= '|')
        else:
            print(jogo, end= '|')
    return jogadas
def jogada_jogadorX():
    erro = True
    while erro == True:
        try:
            jogadaX = int(input ('Jogador X, você quer jogar X em qual posição? '))
            c1 = 0
            for jogo in jogadas:
                if jogo == jogadaX:
                    if jogadas [c1] != 'O':
                        jogadas[c1] = 'X'
                        erro = False
                    else:
                        print ('JOGADA INVÁLIDA')
                c1 = c1 + 1
        except:
            print ('JOGADA INVÁLIDA')
    return jogadas, jogadaX
def jogada_jogadorO():
    erro = True
    while erro == True:
        try:
            jogadaO = int(input ('Jogador O, você quer jogar O em qual posição? '))
            c1 = 0
            for jogo in jogadas:
                if jogo == jogadaO:
                    if jogadas [c1] != 'X':
                        jogadas[c1] = 'O'
                        erro = False
                    else:
                        print ('JOGADA INVÁLIDA')
                c1 = c1 + 1
        except:
            print ('JOGADA INVÁLIDA')
    return jogadas, jogadaO
def verificar_vitoria():
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for c in combinacoes:
        if jogadas[c[0]] == jogadas[c[1]] == jogadas[c[2]]:
            if jogadas[c[0]] == 'X':
                print('JOGADOR X VENCEU')
                return False, True
            elif jogadas[c[0]] == 'O':
                print('JOGADOR O VENCEU')
                return True, False
    return False, False
def verificar_empate ():
    q = 0
    for jogada in jogadas:
        if jogada == 'O' or jogada == 'X':
            q +=1
    if q == 9:
        print ('JOGO EMPATOU')
        a = True
        return True
    else:
        return False
while vitoriaX == False and vitoriaO == False:
    c=c+1
    limpar_tela()
    mostrar_tabuleiro()
    print()
    if c%2 == 1:
        jogada_jogadorX ()
    if c%2 == 0:
        jogada_jogadorO()
    vitoriaO, vitoriaX = verificar_vitoria()
    a = verificar_empate()
    limpar_tela()
    if a == True:
        break
mostrar_tabuleiro()
print()
verificar_vitoria()
if a == True:
    print ('O JOGO EMPATOU')