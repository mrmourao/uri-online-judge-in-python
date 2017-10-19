valores = input().split()
valores = list(map(float,valores))

A, B, C = valores

if(A+B > C and B+C > A and A+C > B ):
    print("Perimetro = %.1f" %(A+B+C))
else:
    print("Area = %.1f" %(0.5*(A+B)*C))