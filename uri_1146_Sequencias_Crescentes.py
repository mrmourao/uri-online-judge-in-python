while True:
    v = int(input())
    if(v == 0):
        break
        
    r = ""
    for i in range(1,v+1):
        r += str(i) + " "
    print(r[:-1])