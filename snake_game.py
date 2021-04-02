import pygame, CSSColors
from pygame.locals import *
from sys import exit
from random import randint



#--------------------------------------------- declared variables -----------------------------------------------------#

width = 600
height = width

x_snake = int(width / 2)//20*20
y_snake = int(height / 2)//20*20

x_apple = (randint(20, 580))//20*20
y_apple = (randint(20, 580))//20*20

velocidade = 20
x_control = velocidade
y_control = 0

pontos = 0

list_snake = []
complimento_inicial = 4
died = False

#---------------------------------------------- configuração padrão -----------------------------------------------------#


pygame.init()                                           # da inicio ao pygame.
tela = pygame.display.set_mode((height, width))         # constroi um display é passado a largura e autura como parametro.
pygame.display.set_caption('Snake_Game')                # define o nome da aplicação.
clock = pygame.time.Clock()                             # inicia o um relogio para dar inicio aos FPS.
fonte = pygame.font.SysFont('arial', 30, True, False)
fonte2 = pygame.font.SysFont('arial', 20, True, True)

#---------------------------------------------- definindo funções -------------------------------------------------------#

def on_grid_apple_random():
    global x_apple,y_apple
    x_apple = (randint(20, 590))//20*20
    y_apple = (randint(20, 590))//20*20

def snake_plus_plus(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(tela, CSSColors.lime_green, (XeY[0], XeY[1], 20, 20))

def restart_game():
    global pontos,complimento_inicial,x_snake,y_snake,lista_cabeca,list_snake,x_apple,y_apple,died
    pontos = 0
    complimento_inicial = 2
    x_snake = int(width/2)//20*20
    y_snake = int(height/2)//20*20
    lista_cabeca = []
    list_snake = []
    on_grid_apple_random()
    died = False

def game_over():
    global fonte2,msn2,text_game_over,rect_text,event,died

    msn2 = 'GAME OVER aperte R para reiniciar'
    text_game_over = fonte2.render(msn2,True,CSSColors.blue)
    rect_text =  text_game_over.get_rect()
    died = True
    while died:
        tela.fill(CSSColors.black)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()
        rect_text.center = (width // 2, height // 2)
        tela.blit(text_game_over,rect_text)
        pygame.display.update()

def control_movement():
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
    global x_snake, y_snake, height, width

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0

def grip():
    global x_apple,y_apple,complimento_inicial,pontos
    
    on_grid_apple_random()
    complimento_inicial += 1
    pontos += 1

def size_snake():
    global list_snake,lista_cabeca

    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)
    list_snake.append(lista_cabeca)

while True:
    clock.tick(20)
    tela.fill(CSSColors.black)
    snake = pygame.draw.rect(tela, CSSColors.lime_green, (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, CSSColors.orange_red, (x_apple, y_apple, 20, 20))
    
    HUD = f'PONTOS: {pontos}'
    texto_formatado = fonte.render(HUD, False, CSSColors.antique_white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            control_movement()
        x_snake = x_snake + x_control
        y_snake = y_snake + y_control

        if snake.colliderect(apple):
            grip()

        lista_cabeca = []

        size_snake()

        if list_snake.count(lista_cabeca) > 1:
            game_over()

        border_colision()

        if len(list_snake) > complimento_inicial:
            del list_snake[0]

    tela.blit(texto_formatado, (10, 10))
    snake_plus_plus(list_snake)
    pygame.display.update()