while True:
    v = input().split(" ")
    h1,m1,h2,m2 = v
    h1 = int(h1)
    m1 = int(m1)
    m2 = int(m2)
    h2 = int(h2)
    
    if((h1+m1+h2+m2)==0):
        break
    
    hr_ini = 0
    hr_fin = 0
    
    if(h1 == 0):
        hr_ini = 24*60 + m1
    else:
        hr_ini = h1*60 + m1
    if(h2 == 0):
        hr_fin = 24*60 + m2
    else:
        hr_fin = h2*60 + m2
             
    if(hr_fin > hr_ini):
        print(hr_fin-hr_ini)
    else:
        print(24*60 - (hr_ini-hr_fin))