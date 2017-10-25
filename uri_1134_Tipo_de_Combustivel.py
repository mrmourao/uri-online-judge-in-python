valor = 0
a = 0
g = 0
d = 0

while valor != 4:
    valor = int(input())
    
    if(valor == 1):
        a += 1
    
    if(valor == 2):
        g += 1
    
    if(valor == 3):
        d += 1

print("MUITO OBRIGADO")
print("Alcool: %d" %a)
print("Gasolina: %d" %g)
print("Diesel: %d" %d)