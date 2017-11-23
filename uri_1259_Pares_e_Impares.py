qte = int(input())

pares = []
impares = []
for n in range(qte):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort(reverse=True)

for p in pares:
    print(p)

for i in impares:
    print(i)