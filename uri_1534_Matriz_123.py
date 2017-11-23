while True:
    try:
        N = int(input())

        resultado =  []

        col2 = N - 1
        for i in range(N):
            tmp = []
            for j in range(N):
                if(j==col2):
                    tmp.append(2)
                    col2 -= 1
                else:
                    if(i == j):
                        tmp.append(1)
                    else:
                        tmp.append(3)
            resultado.append(tmp)

        for i in range(N):
            tx = ''
            for j in range(N):
                tx += str(resultado[i][j])
            print(tx)
    except EOFError:
        break