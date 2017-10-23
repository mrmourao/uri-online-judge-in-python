v1 = int(input())
v2 = int(input())

soma = 0

if(v1>v2):
    t=v1
    v1=v2
    v2=t

if(v1%2 != 0):
    v1 += 2
    while(v1 < v2):
        if(v1%2 !=0):
            soma += v1
        v1 += 1
else:
    v1 += 1
    while(v1 < v2):
        if(v1%2 !=0):
            soma += v1
        v1 += 1

print(soma)