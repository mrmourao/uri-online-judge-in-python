v_i = 0
v_g = 0
e = 0

while True:
    g_i,g_g = list(map(int,input().split()))
    if(g_i == g_g):
        e += 1
    else:
        if(g_i < g_g):
            v_g += 1
        else:
            v_i += 1
    
    print("Novo grenal (1-sim 2-nao)")
    escolha = int(input())
    if(escolha == 2):
        break

print("%d grenais" %(v_i+v_g+e))
print("Inter:%d" %v_i)
print("Gremio:%d" %v_g)
print("Empates:%d" %e)

if(v_i == v_g):
    print("Nao houve vencedor")
else:
    if(v_i > v_g):
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")