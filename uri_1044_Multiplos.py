valores = input().split()
valores = list(map(int,valores))

A, B = valores

if (B%A == 0) or (A%B == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')