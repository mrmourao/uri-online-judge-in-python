import re

qte = int(input())

for i in range(qte):
    texto = input()
    texto_new = ''

    for l in texto:
        if re.match("[a-zA-Z]", l):
            texto_new += chr(ord(l)+3)
        else:
            texto_new += l

    texto_new = texto_new[::-1]
    meio = int((len(texto_new)/2))
    metade1 = texto_new[0:meio]
    metade2 = texto_new[meio:]
    metade_new = ''

    for l in metade2:
        metade_new += chr(ord(l)-1)

    texto_final = metade1+metade_new

    print(texto_final)