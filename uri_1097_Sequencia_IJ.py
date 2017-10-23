i = 1
j = 7

while(i<10):
    for x in range(3):
        print("I=%d J=%d" %(i,j))
        j += -1
    i += 2
    j = i + 6