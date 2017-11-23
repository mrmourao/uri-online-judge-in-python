while True:
    qte = int(input())

    if qte == 0:
        break
    A,B = [0,0]

    for i in range(qte):
        n1, n2 = list(map(int,input().split()))
        if n1>n2:
            A += 1
        if n1<n2:
            B += 1
    print("%d %d" %(A,B))
