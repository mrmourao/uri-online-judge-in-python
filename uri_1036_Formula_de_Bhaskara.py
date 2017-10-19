import math
valores = input().split()
A, B, C = valores

A = float(A)
B = float(B)
C = float(C)

r1 = 0
r2 = 0

calc = (B**2)-(4*A*C)

if(calc <0 or A==0):
    print("Impossivel calcular")
else:
    calc=math.sqrt(calc)
    r1 = (-B+calc)/(2*A)
    r2 = (-B-calc)/(2*A)
    print("R1 = %.5f\nR2 = %.5f" %(r1,r2))