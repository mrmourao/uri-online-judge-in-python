qte = int(input())

for i in range(qte):
    v1,v2 = list(map(int,input().split()))
    soma = 0
    
    if(v1==v2):
        print(0)
    else:
        tmp = 0
        if(v1 > v2):
            tmp = v1
            v1 = v2
            v2 = tmp

        while(v1 < (v2-1)):
            v1 += 1
            
            if(v1%2 != 0):
                soma += v1
                
        print(soma)
        