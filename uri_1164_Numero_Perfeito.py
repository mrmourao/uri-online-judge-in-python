qte = int(input())

for q in range(qte):
    n = int(input())
    soma = 0
    for i in range(1,n):
        if(n%i == 0):
            soma += i
    if(soma == n):
        print("%d eh perfeito" %n)
    else:
        print("%d nao eh perfeito" %n)