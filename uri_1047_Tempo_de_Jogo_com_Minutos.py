valores = input().split()
valores = list(map(int,valores))

a, b, c, d = valores
    
inicio = a*60 + b
final = c*60 + d
duracao = 0

if(a <= c):
    duracao = final - inicio
    if(duracao == 0):
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(24,duracao%60))
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((duracao - duracao%60)/60,duracao%60))
else:
    duracao = (24*60 - inicio) + final
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((duracao - duracao%60)/60,duracao%60))