qte = int(input())

for i in range(qte):
    texto = input()
    qte = int(input())
    t_new = ''
    for l in texto:
        posicao = ord(l)-qte

        if(posicao < 65):
            t_new += chr(91-(65-posicao))
        else:
            t_new += chr(ord(l)-qte)
    print(t_new)