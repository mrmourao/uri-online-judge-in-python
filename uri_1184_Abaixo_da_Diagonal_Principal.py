op = input()
soma = 0
c_out = 12
c_in = 0
qte = 0
nao_entra = c_out
entra = c_in

for i in range(144):
	valor = float(input())

	if(nao_entra + entra == 0):
		c_out -= 1
		c_in += 1
		nao_entra = c_out
		entra = c_in

	if (entra > 0):
		entra -= 1
		soma += valor
		qte += 1
		continue

	if (nao_entra > 0):
		nao_entra -= 1
		continue
		
if(op == 'S'):
	print('%.1f' %soma)
else:
	print('%.1f' %(soma/float(qte)))