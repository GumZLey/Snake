import pygame
import time
import random


pygame.init()
pygame.display.set_caption("Snake game by Ley.")

window_width = 600
window_height = 400

window = pygame.display.set_mode((window_width,window_height))


gameover = False

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10


clock = pygame.time.Clock()
snake_speed = 20

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score : " + str(score), True, yellow)
    window.blit(value, [0,0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0] , x[1], snake_block, snake_block])


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [(window_width/5) - 40 , window_height/3])

def gameLoop():
    gameover = False
    game_close = False

    x1 = window_width/2
    y1 = window_height/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1


    foodx = round(random.randrange(0, window_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, window_height - snake_block) / 10) * 10

    while not gameover:

        while game_close == True:
            window.fill(blue)
            message("You Lost! Press C => Playagain or Q => Quit" , red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 > window_width:
            x1 = 0
        if x1 < 0:
            x1 = window_width
        if y1 > window_height:
            y1 = 0
        if y1 < 0:
            y1 = window_height

        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        print(snake_head)
        print(snake_List)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake-1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, window_height - snake_block) / 10) * 10
            Length_of_snake +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()






