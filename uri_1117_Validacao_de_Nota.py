soma = 0
qte = 0
while qte < 2:
    nota = float(input())
    if(nota >= 0 and nota <= 10):
        soma += nota
        qte += 1
    else:
        print("nota invalida")

print("media = %.2f" %(soma/2))