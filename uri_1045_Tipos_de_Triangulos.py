valores = input().split()
valores = list(map(float,valores))

A,B,C = sorted(valores)[::-1]

continua = True

if(A >= B+C):
    print("NAO FORMA TRIANGULO")
    continua = False

if(A**2 == (B**2) + (C**2) and continua):
    print("TRIANGULO RETANGULO")

if(A**2 > (B**2) + (C**2) and continua):
    print("TRIANGULO OBTUSANGULO")

if(A**2 < (B**2) + (C**2) and continua):
    print("TRIANGULO ACUTANGULO")

if(A == B and B == C and continua):
    print("TRIANGULO EQUILATERO")

if((A == B or B == C) and not (A == B and B == C) and continua):
    print("TRIANGULO ISOSCELES")