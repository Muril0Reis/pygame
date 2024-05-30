import pygame as raceGame 
#imagens a serem carregadas
imagemPrincipal = raceGame.image.load("./imagensOficiais/carroPrincipal.png")
carro2 = raceGame.image.load("./imagensOficiais/carroLaranja.png")
carro1 = raceGame.image.load("./imagensOficiais/carroCinza.png")
background = raceGame.image.load("./imagensOficiais/fundo.png")
faixa = raceGame.image.load("./imagensOficiais/faixa.png")

#inicializar os recursos do pygame
raceGame.init()
fonte = raceGame.font.SysFont('arial',35)
colisao = 0

musica_de_fundo = raceGame.mixer.music.load('Top Gear - Track 1 (Super Nintendo) (320).mp3')
raceGame.mixer.music.play(-1)

#definindo os parâmetros da janela
tela = raceGame.display.set_mode((800,600))

#definir o título da janela
raceGame.display.set_caption("HENRY´S RACING") 

emExecucao = True
carroX = 200
carroY = 300
cinzaY = -40
laranjaY = -120

def movimentarCarro(x:int,y:int):
    tela.blit(raceGame.transform.scale_by(imagemPrincipal,0.7),(x,y))
def gerarFundoDaTela():
    tela.blit(raceGame.transform.scale(background,(800,600)),(0,0))
    tela.blit(raceGame.transform.scale(faixa,(20,200)),(400,0))
    tela.blit(raceGame.transform.scale(faixa,(20,200)),(400,250))
    tela.blit(raceGame.transform.scale(faixa,(20,200)),(400,500))
    tela.blit(raceGame.transform.scale(carro1,(189,189)),(200,cinzaY))
    tela.blit(raceGame.transform.scale(carro2,(189,189)),(400,laranjaY))

while emExecucao == True:
    mensagem = f'Colisão: {colisao}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in raceGame.event.get():
        if event.type == raceGame.QUIT:
            emExecucao = False
    #COMANDOS PARA MOVIMENTOS
    if raceGame.key.get_pressed()[raceGame.K_LEFT]:
        print("Esquerda")
        carroX = carroX - 3
    if raceGame.key.get_pressed()[raceGame.K_RIGHT]:
        print("Direita")
        carroX = carroX + 3
    if raceGame.key.get_pressed()[raceGame.K_UP]:
        print("Cima")
        carroY = carroY - 3
    if raceGame.key.get_pressed()[raceGame.K_DOWN]:
        print("Desce")
        carroY = carroY + 3

    #CARROS PASSANDO
    cinzaY = cinzaY + 2
    if cinzaY >= 600:
        cinzaY = -40
    laranjaY = laranjaY + 2
    if laranjaY >= 600:
        laranjaY = -120
    
    #COLISÃO
    if carroY and carroX == cinzaY:
        print('colidiu')
        colisao = colisao + 1
    if carroY and carroX == laranjaY:
        print('colidiu')
        colisao = colisao + 1
    
    gerarFundoDaTela()
    movimentarCarro(carroX,carroY)
    tela.blit(texto_formatado, (650,30))
    raceGame.display.update()
    