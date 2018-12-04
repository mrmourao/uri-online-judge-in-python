# -*- coding: utf-8 -*-
willContinue = True

while willContinue == True:
    firstLine = input()
    firstLine = firstLine.split(" ")

    if firstLine[0] != "0" and firstLine[1] != "0":
        secondLine = input()
        rolls = int(input())
        secondLine = secondLine.split(" ")
        

        players = int(firstLine[0])
        squares = int(firstLine[1])
        squares = squares + 1
        
        traps = [int(secondLine[0]), int(secondLine[1]), int(secondLine[2])]
        
        playerState = (players+1)*[0]
        playerPosition = (players+1)*[0]
        
        for cont in range(0,players):
            playerState[cont] = "OK"
            playerPosition[cont] = 0
        
        playerTurn = 0
        rollCont = 0
        winner = 200
        while rollCont < rolls:
            vaiJogar = True
            if playerState[playerTurn] == "TRAPPED":
                playerState[playerTurn] = "OK"
                playerTurn = playerTurn+1
                vaiJogar = False
        
            elif playerState[playerTurn] == "OK" and vaiJogar == True:
                dices = input()
                dices = dices.split(" ")
                result = int(dices[0]) + int(dices[1]) + playerPosition[playerTurn]
                playerPosition[playerTurn] = result
                for contTrap in range(0,3):
                    if result == traps[contTrap]:
                        playerState[playerTurn] = "TRAPPED"
        
            if playerPosition[playerTurn] >= squares and winner == 200:
                winner = playerTurn
        
            if vaiJogar == True:
                rollCont = rollCont + 1
                playerTurn = playerTurn + 1
            if playerTurn == players:
                playerTurn = 0

        winner = winner + 1
        print(winner)

    elif firstLine[0] == "0" and firstLine[1] == "0":
        willContinue = False
