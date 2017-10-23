lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

pares = 0

for v in lista:
    if(v%2 == 0):
        pares += 1

print("%d valores pares" %pares)
