qte = int(input())

for i in range(qte):
    texto = input()
    
    if(len(texto)>3):
        print(3)
    else:
        soma = 0
        if (texto[0:1]=='o'):
            soma += 1
        if (texto[1:2]=='n'):
            soma += 1
        if (texto[2:3]=='e'):
            soma += 1
        
        if(soma>=2):
            print(1)
        else:
            print(2)