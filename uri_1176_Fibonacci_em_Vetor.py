tabela=[0,1]
anterior=0
atual=1

for i in range(60):
    tnp = atual+anterior
    tabela.append(tnp)
    anterior=atual
    atual=tnp

qte = int(input())
for i in range(qte):
    valor = int(input())
    print('Fib(%d) = %d' %(valor, tabela[valor]))