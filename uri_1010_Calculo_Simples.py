linha1 = input().split(" ")
linha2 = input().split(" ")

cod1,qt1,vl1 = linha1
cod2,qt2,vl2 = linha2

cod1 = int(cod1)
qt1 = int(qt1)
vl1 = float(vl1)
cod2 = int(cod2)
qt2 = int(qt2)
vl2 = float(vl2)

total = (qt1*vl1) + (qt2*vl2)

print("VALOR A PAGAR: R$ %.2f" %total)