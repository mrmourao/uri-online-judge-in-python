idade = 0
soma = 0
qte = 0

while True:
    idade = int(input())
    if(idade >= 0):
        soma += idade
        qte += 1
    else:
        break

print("%.2f" %(soma/float(qte)))