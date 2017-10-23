lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

pares = 0
impares = 0
positivos = 0
negativos = 0

for v in lista:
    if(v%2 == 0):
        pares += 1
    else:
        impares += 1
    
    if(v > 0):
        positivos += 1
    else:
        if(v < 0):
            negativos += 1

print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivos)
print("%d valor(es) negativo(s)" %negativos)