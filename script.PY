import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
largura = 640
altura = 480
x = largura / 2
y = altura / 2
x_azul = randint(40, 600)
y_azul = 0
x_vermelho = randint(40, 600)
y_vermelho = 400
jogo_ativo = True

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')
relogio = pygame.time.Clock()
velocidade_azul = 5

while jogo_ativo:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[K_a] and x_vermelho > 0:  
        x_vermelho -= 10
    if keys[K_d] and x_vermelho < largura - 50:  
        x_vermelho += 10

    ret_vermelho = pygame.draw.rect(tela, (255, 12, 46), (x_vermelho, y_vermelho, 50, 50))
    ret_azul = pygame.draw.rect(tela, (100, 255, 100), (x_azul, y_azul, 40, 50))
    chao = pygame.draw.rect(tela, (40, 255, 40), (0, 450, largura, 30))

    if ret_vermelho.colliderect(ret_azul):        
        x_azul = randint(40, 600)
        y_azul = 0
        pontos += 1

    y_azul += 5
    if ret_azul.colliderect(chao):
        jogo_ativo = False
        print ("você perdeu")
    if pontos >= 10:
        velocidade_azul = velocidade_azul + 5
    if pontos >= 15:
        velocidade_azul = velocidade_azul + 5
    if pontos >= 25:
        velocidade_azul = velocidade_azul + 10

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
