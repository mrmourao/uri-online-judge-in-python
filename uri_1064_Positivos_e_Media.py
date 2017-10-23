lista = []
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

positivos = 0
soma = 0.0

for v in lista:
    if(v>0):
        positivos += 1
        soma += v

media = soma / float(positivos)
print("%d valores positivos" %positivos)
print("%.1f" %media)