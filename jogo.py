import pygame
from personagem import Personagem
from obstaculo import Obstaculo


# # Inicialize o Pygame
# pygame.init()

# # Carregue o arquivo de som
# som = pygame.mixer.Sound("musica_fundo.wav")

# # Reproduza o som
# som.play()

# # Mantenha o programa em execução até que o som termine de tocar
# while pygame.mixer.get_busy():
#     pygame.time.delay(100)

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("pior jogo de todos")
tela.fill((0,187,255))

FUNDO = pygame.image.load("imagens/floresta.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/macaco.png",130,130,400,370)
jogador2 = Personagem("imagens/bode.png",110,110,370,370)

lista_comida = [Obstaculo("imagens/uva.png",80,50,100,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/uva.png",80,50,20,0),
               Obstaculo("imagens/uva.png",80,50,20,0),
               Obstaculo("imagens/uva.png",80,50,20,0),
               Obstaculo("imagens/uva.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,500,0),
               Obstaculo("imagens/plastico.png",80,50,500,0),
               Obstaculo("imagens/plastico.png",80,50,500,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/banana.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/morango.png",80,50,20,0),
               Obstaculo("imagens/abacaxi.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),
               Obstaculo("imagens/plastico.png",80,50,20,0),]
#.
#Configurando a fonte
# fonte = pygame.font.SysFont("Castellar",14)



#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

    #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)
    jogador2.movimentar_via_controle(pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)
    jogador2.desenhar(tela)
    

    for comida in lista_comida:
        comida.movimenta()
        comida.desenhar(tela)

        if jogador1.mascara.overlap(comida.mascara,(comida.pos_x-jogador1.pos_x , comida.pos_y-jogador1.pos_y)):
            jogador1.pos_x = 300
            jogador1.pos_y = 450
            jogador1.pontuacao -= 1

        if jogador2.mascara.overlap(comida.mascara,(comida.pos_x-jogador2.pos_x , comida.pos_y-jogador2.pos_y)):
            jogador2.pos_x = 450
            jogador2.pos_y = 450
            jogador2.pontuacao -= 1

        if jogador1.pos_y <= 10:
            jogador1.pos_x = 300
            jogador1.pos_y = 450
            jogador1.pontuacao += 1

        if jogador2.pos_y <= 10:
            jogador2.pos_x = 300
            jogador2.pos_y = 450
            jogador2.pontuacao += 1
        
    # texto_pontuacao_vaca = fonte.render(f"Pontuação da VACA: {jogador1.pontuacao}",True,(255,0,0))
    # tela.blit(texto_pontuacao_vaca,(0,10))

    # texto_pontuacao_hamster= fonte.render(f"Pontuação da HAMSTER: {jogador2.pontuacao}",True,(255,0,0))
    # tela.blit(texto_pontuacao_hamster,(0,24))

    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)