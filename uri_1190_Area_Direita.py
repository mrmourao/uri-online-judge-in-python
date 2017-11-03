op = input()
soma = 0
c_out = 10
c_in = 1
mudar = False

qte = 0
nao_entra = c_out
entra = c_in


for i in range(144):
	valor = float(input())

	if(i < 23):
		continue

	if (mudar):
		if(nao_entra + entra == 0):
			c_out += 1
			c_in -= 1

			if(i == 79):
				c_in = 5

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
		
		break
	else:
		if(nao_entra + entra == 0):
			c_out -= 1
			c_in += 1
			nao_entra = c_out
			entra = c_in	

		if (entra > 0):
			if(entra == 5):
				mudar = True
				c_in = 5
				c_out = 7
				nao_entra = c_out

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