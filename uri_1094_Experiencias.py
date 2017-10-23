qte = int(input())
qte_total = 0
qte_r = 0
qte_c = 0
qte_s = 0

for i in range(qte):
    valores = input().split()
    quantia, tipo = valores
    qte_total += int(quantia)
    
    if(tipo == "C"):
        qte_c += int(quantia)
    else:
        if(tipo == "R"):
            qte_r += int(quantia)
        else:
            qte_s += int(quantia)

print("Total: %d cobaias" %qte_total)
print("Total de coelhos: %d" %qte_c)
print("Total de ratos: %d" %qte_r)
print("Total de sapos: %d" %qte_s)
print("Percentual de coelhos: {:.2f} %".format((qte_c/float(qte_total))*100))
print("Percentual de ratos: {:.2f} %".format((qte_r/float(qte_total))*100))
print("Percentual de sapos: {:.2f} %".format((qte_s/float(qte_total))*100))