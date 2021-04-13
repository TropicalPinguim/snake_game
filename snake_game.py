import pygame
from pygame.locals import *
from random import randint
#--------------------------------------------- declared variables -----------------------------------------------------#
new_real_score = 0
speed = 8
moving = 20
scale = moving
x_control = moving
y_control = 0
real_score = 0
list_snake = []
complimento_inicial = 4
died = False
#---------------------------------------------------- colors ----------------------------------------------------------#

GREEN_SNAKE = (134, 180, 96)
RED_APPLE = (191, 91, 91)
BLUE = (60, 141, 136)
BLACK = (89, 87, 88)
YELLOW = (198, 185, 85)

#---------------------------------------------- screen Parameters -----------------------------------------------------#

width = 600
height = 640
pygame.init()                                         # da inicio ao pygame.
tela = pygame.display.set_mode((width, height))       # constroi um display é passado a largura e autura como parametro.
pygame.display.set_caption('Snake_Game')              # define o nome da aplicação.
game_icon = pygame.image.load("icon.png")             # indicando o caminho do arquivo, armasenando em uma variavel.
pygame.display.set_icon(game_icon)                    # define o icone da aplicação,
clock = pygame.time.Clock()                           # inicia o um relogio para dar inicio aos FPS.

# -------------------------------------------------- apple Parameters --------------------------------------------------#

x_apple = (randint(0, 580)) // moving * moving
y_apple = (randint(40, 580)) // moving * moving
def random_apple_position():
    global x_apple, y_apple
    x_apple = (randint(0, 580)) // moving * moving
    y_apple = (randint(40, 580)) // moving * moving
    return (x_apple, y_apple)

# -------------------------------------------------- snake Parameters --------------------------------------------------#

x_snake = int(width / 2)//moving*moving
y_snake = int(height / 2)//moving*moving

def snake_plus_plus(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(tela, GREEN_SNAKE, (XeY[0], XeY[1], moving, moving))

def snake_on_grid():
    global x_snake,y_snake

    x_snake = int(width/2)//moving*moving
    y_snake = int(height/2)//moving*moving

def size_snake():
    global list_snake,lista_cabeca

    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)
    list_snake.append(lista_cabeca)

#---------------------------------------------- definindo funções -------------------------------------------------------#

def restart_game():
    global pontos,complimento_inicial,x_snake,y_snake,lista_cabeca,list_snake,x_apple,y_apple,died
    pontos = 0
    complimento_inicial = 2
    snake_on_grid()
    lista_cabeca = []
    list_snake = []
    random_apple_position()
    died = False

def best_best_hiscore():
    global new_real_score, real_score

    if real_score > new_real_score:
        new_real_score = real_score

def game_over():
    global game_over_font, gameover, speed, new_real_score, text_game_over, rect_text, event, died, real_score

    game_over_font = pygame.font.SysFont('Pixelade', 48, True, False)
    gameover = 'GAME OVER'
    text_game_over = game_over_font.render(gameover, False, YELLOW)
    rect_text =  text_game_over.get_rect()
    
    restart_font = pygame.font.SysFont('Pixelade', 28, True, False)
    restart = 'APERTE R PARA CONTINUAR'
    text_restart = restart_font.render(restart, False, YELLOW)
    rect_text2 =  text_restart.get_rect()

    died = True

    while died:
        tela.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    best_best_hiscore()
                    real_score = 0
                    speed = 8
                    restart_game()
        rect_text.center = (width // 2, (height // 2)-20)
        rect_text2.center = (width // 2, (height // 2)+10)
        tela.blit(text_game_over,rect_text)
        tela.blit(text_restart,rect_text2)
        pygame.display.update()

def control_movement():
    global x_control, y_control
    if event.type == KEYDOWN:
        if event.key == K_a:
            if x_control == moving:
                pass
            else:
                x_control = -moving
                y_control = 0
        if event.key == K_d:
            if x_control == -moving:
                pass
            else:
                x_control = moving
                y_control = 0
        if event.key == K_s:
            if y_control == -moving:
                pass
            else:
                x_control = 0
                y_control = moving
        if event.key == K_w:
            if y_control == moving:
                pass
            else:
                x_control = 0
                y_control = -moving

def border_colision():
    global x_snake, y_snake, height, width

    if x_snake > width:
        x_snake = -20
    if x_snake < -20:
        x_snake = width
    if y_snake < 20:
        y_snake = height 
    if y_snake > height:
        y_snake = 20

def grip():
    global x_apple, y_apple, complimento_inicial, real_score, speed
    
    random_apple_position()
    complimento_inicial += 1
    real_score += 1
    speed = speed + 0.8

def HUD():
    global background, new_real_score, hud_score, text_score, hud_font, best_hud_score, text_best_score
    best_best_hiscore()
    hud_font = pygame.font.SysFont('Pixelade', 22, True, False)
    background = pygame.draw.rect(tela, BLUE, (0, 0, width, 40))

    best_hud_score = f'BEST SCORE: {new_real_score}'
    text_best_score = hud_font.render(best_hud_score, False, YELLOW)
    tela.blit(text_best_score, (6, 6))

    hud_score = f'SCORE: {real_score}'
    text_score = hud_font.render(hud_score, False, YELLOW)
    tela.blit(text_score, (6, 24))

while True:
    clock.tick(speed)
    tela.fill(BLACK)
    snake = pygame.draw.rect(tela, GREEN_SNAKE, (x_snake, y_snake, scale, scale))
    apple = pygame.draw.rect(tela, RED_APPLE, (x_apple, y_apple, scale, scale))
    for event in pygame.event.get():     
        if event.type == QUIT:
            pygame.quit()
        control_movement()
    x_snake = x_snake + x_control
    y_snake = y_snake + y_control
    lista_cabeca = []
    size_snake()
    if snake.colliderect(apple):
        grip()
    if list_snake.count(lista_cabeca) > 1:
        game_over()
    border_colision()
    if len(list_snake) > complimento_inicial:
        del list_snake[0]
    snake_plus_plus(list_snake)
    HUD()
    pygame.display.update()