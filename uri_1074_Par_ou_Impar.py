qte = int(input())

for i in range(qte):
    valor = int(input())
    if(valor%2 == 0):
        if(valor == 0):
            print("NULL")
        if(valor > 0):
            print("EVEN POSITIVE")
        else:
            if(valor < 0):
                print("EVEN NEGATIVE")
    else:
        if(valor > 0):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")