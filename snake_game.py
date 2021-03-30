import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#--------------------------------------------- declared variables -----------------------------------------------------#
larger = 640
altura = 480

x_snake = int(larger / 2)
y_snake = int(altura / 2)

x_apple = int(randint(40, 600))
y_apple = int(randint(50, 430))

velocidade = 10
x_control = velocidade
y_control = 0

pontos = 0

fonte = pygame.font.SysFont('arial', 30, True, False)
fonte2 = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((larger, altura))

pygame.display.set_caption('Snake_Game')  # essa string represent o nome da aplicação

clock = pygame.time.Clock()

list_snake = []
complimento_inicial = 5

died = False

def snake_plus_plus(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos,complimento_inicial,x_snake,y_snake,lista_cabeca,list_snake,x_apple,y_apple,died
    pontos = 0
    complimento_inicial = 5
    x_snake = int(larger/2)
    y_snake = int(altura / 2)
    lista_cabeca = []
    list_snake = []
    x_apple = int(randint(40, 600))
    y_apple = int(randint(50, 430))
    died = False

def game_over():
    global fonte2,msn2,text_game_over,rect_text,event,died

    msn2 = 'GAME OVER aperte R para reiniciar'
    text_game_over = fonte2.render(msn2,True,(0,0,0))
    rect_text =  text_game_over.get_rect()
    died = True
    while died:
        tela.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar_jogo()
        rect_text.center = (larger // 2, altura // 2)
        tela.blit(text_game_over,rect_text)
        pygame.display.update()

def movimento():
    global x_control, y_control
    if event.key == K_a:
        if x_control == velocidade:
            pass
        else:
            x_control = -velocidade
            y_control = 0
    if event.key == K_d:
        if x_control == -velocidade:
            pass
        else:
            x_control = velocidade
            y_control = 0
    if event.key == K_s:
        if y_control == -velocidade:
            pass
        else:
            x_control = 0
            y_control = velocidade
    if event.key == K_w:
        if y_control == velocidade:
            pass
        else:
            x_control = 0
            y_control = -velocidade

def border_colision():
    global x_snake, y_snake, altura, larger

    if x_snake > larger:
        x_snake = 0
    if x_snake < 0:
        x_snake = larger
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0

def peguei():
    global x_apple,y_apple,complimento_inicial,pontos

    x_apple = int(randint(40, 600))
    y_apple = int(randint(50, 430))
    complimento_inicial += 1
    pontos += 1

def tamanho_snake():
    global list_snake,lista_cabeca

    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)
    list_snake.append(lista_cabeca)

while True:
    clock.tick(30)
    tela.fill((255, 255, 255))
    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 20, 20))
    HUD = f'PONTOS: {pontos}'
    texto_formatado = fonte.render(HUD, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            movimento()
        x_snake = x_snake + x_control
        y_snake = y_snake + y_control

        if snake.colliderect(apple):
            peguei()
        lista_cabeca = []
        tamanho_snake()
        if list_snake.count(lista_cabeca) > 1:
            game_over()
        border_colision()
        if len(list_snake) > complimento_inicial:
            del list_snake[0]

        tela.blit(texto_formatado, (450, 40))
        snake_plus_plus(list_snake)
        pygame.display.update()