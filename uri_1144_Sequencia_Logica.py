n = int(input())
n1 = 1

for i in range(1,(n*2)+1):
    if(i%2 == 0):
        print("%d %d %d" %(n1,(n1**2)+1,(n1**3)+1))
        n1 += 1
    else:
        print("%d %d %d" %(n1,n1**2,n1**3))  
