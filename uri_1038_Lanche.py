valores = input().split()
codigo, qte = valores

qte = int(qte)

tab_preco = {"1":4.0, "2":4.5,"3":5.0,"4":2.0,"5":1.5}

resultado = qte * tab_preco[codigo]

print('Total: R$ %.2f' %resultado)