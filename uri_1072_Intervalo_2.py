qte = int(input())

sim = 0
nao = 0

for i in range(qte):
    valor = int(input())
    if(valor >= 10 and valor <= 20):
        sim += 1
    else:
        nao += 1

print("%d in" %sim)
print("%d out" %nao)