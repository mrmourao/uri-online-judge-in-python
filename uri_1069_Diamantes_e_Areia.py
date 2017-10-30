qte = int(input())

for i in range(qte):
	linha = input()
	total = 0
	menor = 0
	for j in range(len(linha)):
		if(linha[j] == "<"):
			menor += 1
		if(linha[j] == ">" and menor > 0):
			total += 1
			menor -= 1

	print(total)
