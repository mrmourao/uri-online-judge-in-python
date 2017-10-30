qte = int(input())

for i in range(qte):
    soma = 0
    n1, n2 = list(map(int,input().split()))
    for v in range(n2):
        while(n1%2 == 0):
            n1 += 1
        soma += n1
        n1 += 1
    print(soma)           