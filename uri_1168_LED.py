tabela = (6,2,5,5,4,5,6,3,7,6)
n = int(input())

for l in range(n):
    total = 0
    valor = input()
    for v in valor:
        total += tabela[int(v)]
    print("%d leds" %int(total))