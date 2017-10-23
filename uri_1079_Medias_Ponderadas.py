qte = int(input())

for i in range(qte):
    lista = list(map(float,input().split()))
    v1,v2,v3 = lista
    v1 = v1*2
    v2 = v2*3
    v3 = v3*5
    media = (v1+v2+v3)/10
    print("%.1f" %media)