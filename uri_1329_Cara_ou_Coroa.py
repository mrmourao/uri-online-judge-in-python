while 1:
	qte = int(input())

	if (qte == 0):
		break

	resultados = list(map(int,input().split()))
	m = 0
	j = 0
	for v in resultados:
		if(v == 0):
			m += 1
		else:
			j += 1
	print("Mary won %d times and John won %d times" %(m,j))