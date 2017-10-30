while 1:
    n1 = int(input())
    
    if(n1 == 0):
        break
    
    soma = 0    
    for i in range(5):
        while(n1%2 != 0):
            n1 += 1
        soma += n1
        n1 += 1
    print(soma)    