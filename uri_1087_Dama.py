while True:
    vl = input().split(" ")
    x1,y1,x2,y2 = vl

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if (x1 + y1 + x2 + y2) == 0:
        break
    
    if (x1==x2) and (y1==y2):
        print("%d" %0)
        continue
    
    if (x1==x2) or (y1==y2):
        print("%d" %1)
        continue
    
    if abs(x1-x2) == abs(y1-y2):
        print("%d" %1)
        continue
    
    print("%d" %2)