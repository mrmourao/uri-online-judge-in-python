qte = int(input())

for t in range(qte):
    n = int(input())
    primo = True

    for i in range(2,n):
        if(n%i == 0):
            primo = False
            break

    if(primo):
        print("%d eh primo" %n)
    else:
        print("%d nao eh primo" %n)

