lista = []
for i in range(20):    
    valor = int(input())
    lista.append(valor)
pos = 0
for l in lista[::-1]:
    print("N[%d] = %d" %(pos,l))
    pos += 1