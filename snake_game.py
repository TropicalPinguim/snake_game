import pygame
from pygame.locals import *
from random import randint

# --------------------------------------------- declared variables -----------------------------------------------------#
new_real_score = 0
speed = 8
moving = 20
scale = moving
x_control = moving
y_control = 0
real_score = 0
list_snake = []
initial_length = 2
died = False
# ---------------------------------------------------- colors ----------------------------------------------------------#

GREEN_SNAKE = (134, 180, 96)
RED_APPLE = (191, 91, 91)
BLUE = (60, 141, 136)
BLACK = (89, 87, 88)
YELLOW = (198, 185, 85)

# ---------------------------------------------- screen Parameters -----------------------------------------------------#

width = 600
height = 640
pygame.init()  # da inicio ao pygame.
screen = pygame.display.set_mode((width, height))  # constroi um display é passado a largura e autura como parametro.
pygame.display.set_caption('Snake_Game')  # define o nome da aplicação.
game_icon = pygame.image.load("imag\icon.png")  # indicando o caminho do arquivo, armasenando em uma variavel.
pygame.display.set_icon(game_icon)  # define o icone da aplicação,
clock = pygame.time.Clock()  # inicia o um relogio para dar inicio aos FPS.

# -------------------------------------------------- apple Parameters --------------------------------------------------#

x_apple = (randint(0, width - moving)) // moving * moving
y_apple = (randint(40, height - moving)) // moving * moving


def random_apple_position():
    global x_apple, y_apple
    x_apple = (randint(0, width - moving)) // moving * moving
    y_apple = (randint(40, height - moving)) // moving * moving
    return (x_apple, y_apple)


# -------------------------------------------------- snake Parameters --------------------------------------------------#

x_snake = int(width / 2) // moving * moving
y_snake = int(height / 2) // moving * moving


def snake_plus_plus(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(screen, GREEN_SNAKE, (XeY[0], XeY[1], moving, moving))


def snake_on_grid():
    global x_snake, y_snake

    x_snake = int(width / 2) // moving * moving
    y_snake = int(height / 2) // moving * moving


def size_snake():
    global list_snake, head_list

    head_list.append(x_snake)
    head_list.append(y_snake)
    list_snake.append(head_list)


# ---------------------------------------------- definindo funções -------------------------------------------------------#

def grip():
    global initial_length, real_score, speed

    initial_length += 1
    real_score += 1
    speed = speed + 0.8

    random_apple_position()


# ---------------------------------------------- definindo funções -------------------------------------------------------#

def best_best_hiscore():
    global new_real_score, real_score

    if real_score > new_real_score:
        new_real_score = real_score


def restart_game():
    global real_score, speed, initial_length, head_list, list_snake, died

    real_score = 0
    speed = 8
    initial_length = 2
    head_list = []
    list_snake = []
    died = False

    best_best_hiscore()
    random_apple_position()
    snake_on_grid()


def game_over():
    global event, died

    game_over_font = pygame.font.SysFont('Pixelade', 48, True, False)
    gameover = 'GAME OVER'
    text_game_over = game_over_font.render(gameover, False, BLUE)
    rect_text = text_game_over.get_rect()

    restart_font = pygame.font.SysFont('Pixelade', 28, True, False)
    restart = 'APERTE R PARA CONTINUAR'
    text_restart = restart_font.render(restart, False, YELLOW)
    rect_text2 = text_restart.get_rect()

    died = True

    while died:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()
        rect_text.center = (width // 2, (height // 2) - 20)
        rect_text2.center = (width // 2, (height // 2) + 10)
        screen.blit(text_game_over, rect_text)
        screen.blit(text_restart, rect_text2)
        pygame.display.update()


# ---------------------------------------------- definindo funções -------------------------------------------------------#

def on_button_pressed():
    global x_control, y_control
    if event.type == KEYDOWN:
        if event.key == K_a or event.key == K_LEFT:
            if x_control == moving:
                pass
            else:
                x_control = -moving
                y_control = 0
        if event.key == K_d or event.key == K_RIGHT:
            if x_control == -moving:
                pass
            else:
                x_control = moving
                y_control = 0
        if event.key == K_s or event.key == K_DOWN:
            if y_control == -moving:
                pass
            else:
                x_control = 0
                y_control = moving
        if event.key == K_w or event.key == K_UP:
            if y_control == moving:
                pass
            else:
                x_control = 0
                y_control = -moving
        if event.key == K_ESCAPE:
            pygame.quit()


def border_colision():
    global x_snake, y_snake

    if x_snake > width:
        x_snake = -scale
    if x_snake < -scale:
        x_snake = width
    if y_snake < scale:
        y_snake = height
    if y_snake > height:
        y_snake = scale


def HUD():

    best_best_hiscore()
    hud_font = pygame.font.SysFont('Pixelade', 22, True, False)
    background = pygame.draw.rect(screen, BLUE, (0, 0, width, (0.064 * height) // 10 * 10))

    best_hud_score = f'BEST SCORE: {new_real_score}'
    text_best_score = hud_font.render(best_hud_score, False, YELLOW)
    screen.blit(text_best_score, (6, 6))

    hud_score = f'SCORE: {real_score}'
    text_score = hud_font.render(hud_score, False, YELLOW)
    screen.blit(text_score, (6, 24))


# ---------------------------------------------- definindo funções -------------------------------------------------------#


while True:

    clock.tick(speed)
    screen.fill(BLACK)

    snake = pygame.draw.rect(screen, GREEN_SNAKE, (x_snake, y_snake, scale, scale))
    apple = pygame.draw.rect(screen, RED_APPLE, (x_apple, y_apple, scale, scale))
    x_snake = x_snake + x_control
    y_snake = y_snake + y_control
    head_list = []

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        on_button_pressed()
    if snake.colliderect(apple):
        grip()
    if list_snake.count(head_list) > 1:
        game_over()
    if len(list_snake) > initial_length:
        del list_snake[0]
    size_snake()
    border_colision()
    snake_plus_plus(list_snake)
    HUD()
    pygame.display.update()