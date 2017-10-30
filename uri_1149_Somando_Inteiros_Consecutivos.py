lista = list(map(int,input().split()))
n1 = 'I'
n2 = 0
soma = 0
for i in lista:
    if(n1 =='I'):
        n1 = i
    else:
        if(i > 0):
            n2 = i
            break

for i in range(n2):
    soma += n1
    n1 += 1
    
print("%d" %soma)