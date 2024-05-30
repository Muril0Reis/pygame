APENAS SE MOVE QUANDO APERTA A TECLA = CORRESPONDE A APENAS UM MOVIMENTO
    if event.type == raceGame.KEYDOWN:
            if event.key == raceGame.K_LEFT:
                print("Esquerda")
                carroX = carroX - 3
            if event.key == raceGame.K_RIGHT:
                print("Direita")
                carroX = carroX + 3
            if event.key == raceGame.K_UP:
                print("Cima")
                carroY = carroY - 3
            if event.key == raceGame.K_DOWN:
                print("Desce")
                carroY = carroY + 3