coluna = int(input())
op = input()
soma = 0

for i in range(144):
	valor = float(input())
	if (i ==  coluna):
		soma += valor
		coluna += 12
if(op == 'S'):
	print('%.1f' %soma)
else:
	print('%.1f' %(soma/12.0))

