while True:
    try:
        linha = input()
        lista = []
        correct = False
        p1 = 0
        p2 = 0

        for v in linha:
            if (v == '('):
                p1 += 1
                lista.append(v)

            if (v == ')'):
                p2 += 1
                lista.append(v)

        if(len(lista)%2 != 0):
            correct = False
        else:
            if(lista[0] == ')'):
                correct = False
            else:
                if (lista[len(lista)-1] == '('):
                    correct = False
                else:
                    if (p1 != p2):
                        correct = False
                    else:
                        correct = True

        if(correct):
            print("correct")
        else:
            print("incorrect")

    except (EOFError):
        break