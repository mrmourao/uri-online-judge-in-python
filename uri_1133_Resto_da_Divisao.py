n1 = int(input())
n2 = int(input())
t = n1

if(n1 > n2):
    n1 = n2
    n2 = t
    
while(n1 < n2):
    n1 += 1
    if(n1%5 == 2 or n1%5 == 3 and n1 != n2):
        print(n1)