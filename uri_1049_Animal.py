nivel_01 = input()
nivel_02 = input()
nivel_03 = input()

if(nivel_01 == 'vertebrado'):
    if(nivel_02 == 'ave'):
        if(nivel_03 == 'carnivoro'):
            print('aguia')
        else:
            print('pomba')
    else:
        if(nivel_03 == 'onivoro'):
            print('homem')
        else:
            print('vaca')
else:
    if(nivel_02 == 'inseto'):
        if(nivel_03 == 'hematofago'):
            print('pulga')
        else:
            print('lagarta')
    else:
        if(nivel_03 == 'hematofago'):
            print('sanguessuga')
        else:
            print('minhoca')