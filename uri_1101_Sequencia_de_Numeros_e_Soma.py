while True:
    try:
        m,n = list(map(int,input().split()))
        if(m < 1 or n < 1 ):
            break
        tmp = 0

        if(m > n):
            tmp = m
            m = n
            n = tmp
        soma = 0
        resultado = ''
        while(m <= n):
            resultado += str(m) + ' '
            soma += m
            m += 1
        resultado += 'Sum=%d'
        print(resultado %soma)
    except:
        break