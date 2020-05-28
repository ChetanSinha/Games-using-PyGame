import pygame
import random
from pygame.locals import *
# colors and fonts
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gold = (197,179,88)


pygame.init()

screen_w = 700
screen_h = 500
game_window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('SnakesForFun')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def display_text(text, color, x, y):
   screen_text = font.render(text, True, color)
   game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(white)
        display_text('Welcome to Snakes for Fun', black, 100, 300)
        display_text('Press SPACE to Play the game', black,80, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()
        pygame.display.update()
        clock.tick(32)
def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    food_x = random.randint(20, screen_w / 2)
    food_y = random.randint(20, screen_h / 2)
    fps = 12
    score = 0


    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            try:
                with open('snakes_highscore.txt','r') as f:
                    highscore = int(f.readline())
                    if score > highscore:
                        highscore = score
                        with open('snakes_highscore.txt','w') as f2:
                            f2.write(str(score))
                game_window.fill(white)
            except:
                with open('snakes_highscore.txt', "w") as f:
                    f.write(str(score))
                game_window.fill(white)
                highscore = score
                
            display_text(f"Your Score:{score}", red, screen_h / 2 - 10, 30)
            display_text(f"High Score:{highscore}", red, screen_h / 2 - 20,   70)
            display_text("Game Over!", red, screen_h/2, 200)
            display_text('Press ENTER to continue',red, 150, 400)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

                if event.type == pygame.QUIT:
                    exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - 10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 10
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y =  10
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 5
                food_x = random.randint(25, screen_w / 2)
                food_y = random.randint(25, screen_h / 2)
                snake_length += 2

            game_window.fill(white)
            display_text(f'Score:{score}', red, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list ) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_w or snake_y<0 or snake_y>screen_h:
                game_over = True

            plot_snake(game_window, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
# gameLoop()
