valor = int(input())
resutado = str(valor)+'\n'

mod100 = valor%100
if(mod100 == valor):
    resutado += '%d nota(s) de R$ 100,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 100,00\n' % (valor / 100)

mod50 = mod100%50
if(mod50 == mod100):
    resutado += '%d nota(s) de R$ 50,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 50,00\n' % (mod100 / 50)

mod20 = mod50%20
if(mod20 == mod50):
    resutado += '%d nota(s) de R$ 20,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 20,00\n' % (mod50 / 20)

mod10 = mod20%10
if(mod10 == mod20):
    resutado += '%d nota(s) de R$ 10,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 10,00\n' % (mod20 / 10)

mod5 = mod10%5
if(mod5 == mod10):
    resutado += '%d nota(s) de R$ 5,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 5,00\n' % (mod10/ 5)

mod2 = mod5%2
if(mod2 == mod5):
    resutado += '%d nota(s) de R$ 2,00\n' % 0
else:
    resutado += '%d nota(s) de R$ 2,00\n' % (mod5/ 2)

mod1 = mod2%1
if(mod1 == mod2):
    resutado += '%d nota(s) de R$ 1,00' % 0
else:
    resutado += '%d nota(s) de R$ 1,00' % (mod2 / 1)

print(resutado)