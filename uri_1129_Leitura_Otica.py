willContinue = True;
while willContinue:    
    num = int(input())
    if num != 0:
        for cont in range(0,num):
            rawAnswer = input()
            rawAnswer = rawAnswer.split(" ")
            item = "*"
            contMarked = 0;
            for cont2 in range(0,5):
                analisedItem = int(rawAnswer[cont2])
                if analisedItem <= 127:
                    item = cont2+1
                    contMarked = contMarked+1
            if item == 1:
                item = "A"
            elif item == 2:
                item = "B"
            elif item == 3:
                item = "C"
            elif item == 4:
                item = "D"
            elif item == 5:
                item = "E"
            if(contMarked >1):
                item = "*"
            print(item)
    elif num == 0:
        willContinue = False