lista = [0,1,1]

r = "0,1,1"
ant = 1
atual = 1
valor = int(input())

for v in range(valor-3):
    t = atual
    atual += ant
    ant = t
    lista.append(atual)
    
print(str(lista[0:valor]).replace(",","").replace("[","").replace("]",""))
