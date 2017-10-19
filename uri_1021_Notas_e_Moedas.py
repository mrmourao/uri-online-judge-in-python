valor = float(input())
resultado = 'NOTAS:\n'

mod100 = valor%100
if(mod100 == valor):
    resultado += '%d nota(s) de R$ 100.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 100.00\n' % (valor / 100)

mod50 = mod100%50
if(mod50 == mod100):
    resultado += '%d nota(s) de R$ 50.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 50.00\n' % (mod100 / 50)

mod20 = mod50%20
if(mod20 == mod50):
    resultado += '%d nota(s) de R$ 20.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 20.00\n' % (mod50 / 20)

mod10 = mod20%10
if(mod10 == mod20):
    resultado += '%d nota(s) de R$ 10.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 10.00\n' % (mod20 / 10)

mod5 = mod10%5
if(mod5 == mod10):
    resultado += '%d nota(s) de R$ 5.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 5.00\n' % (mod10/ 5)

mod2 = mod5%2
if(mod2 == mod5):
    resultado += '%d nota(s) de R$ 2.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 2.00\n' % (mod5/ 2)

    
resultado += 'MOEDAS:\n'    

mod1 = mod2%1
if(mod1 == mod2):
    resultado += '%d moeda(s) de R$ 1.00\n' % 0
else:
    resultado += '%d moeda(s) de R$ 1.00\n' % (mod2 / 1)

mod1 = mod1*100
mod050 = mod1%50
if(mod050 == mod1):
    resultado += '%d moeda(s) de R$ 0.50\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.50\n' % (mod1 / 50)

mod025 = mod050%25
if(mod025 == mod050):
    resultado += '%d moeda(s) de R$ 0.25\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.25\n' % (mod050 / 25)

mod010 = mod025%10
if(mod010 == mod025):
    resultado += '%d moeda(s) de R$ 0.10\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.10\n' % (mod025 / 10)

mod005 = mod010%5
if(mod005 == mod010):
    resultado += '%d moeda(s) de R$ 0.05\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.05\n' % (mod010 / 5)

mod001 = mod005%1
if(mod001 == mod005):
    resultado += '%d moeda(s) de R$ 0.01' % 0
else:
    resultado += '%d moeda(s) de R$ 0.01' % (mod005 / 1)
    
print(resultado)