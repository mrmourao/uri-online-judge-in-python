n1 = int(input())
n2 = 0

while True:
    n2 = int(input())
    if(n2 > n1):
        break

soma = n1
qte = 1
while(soma < n2):
    soma += n1 + qte
    qte += 1

print(qte)
