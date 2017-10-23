valor = int(input())

qte = 0

while True:
    if(valor%2 != 0):
        qte += 1
        print(valor)
    valor += 1
    if(qte == 6):
        break