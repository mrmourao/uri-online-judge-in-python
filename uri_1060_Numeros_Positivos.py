lista = []
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

pares = 0

for v in lista:
    if(v>0):
        pares += 1

print("%d valores positivos" %pares)