valor = int(input())
ano = int(valor / 365)
mes = int((valor%365/30))
dia = int(valor%365%30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(ano,mes,dia))