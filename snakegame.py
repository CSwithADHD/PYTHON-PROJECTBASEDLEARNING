import pygame
import random

pygame.init()

# Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# Game window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Snake Game")

# Clock & font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Score display
def show_score(score):
    text = font.render("Score: " + str(score), True, black)
    gameWindow.blit(text, [5, 5])

# Game Over display
def game_over_screen():
    text = font.render("Game Over! Press Q to Quit", True, red)
    gameWindow.blit(text, [400, 220])

# Game variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
fps = 30
velocity_x = 0
velocity_y = 0

food_x = random.randint(0, 1200 - snake_size)
food_y = random.randint(0, 500 - snake_size)

snake_list = []
snake_length = 1
score = 0

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and game_over:
                exit_game = True

            if not game_over:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = 10
                    velocity_x = 0
                if event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0

    if not game_over:
        snake_x += velocity_x
        snake_y += velocity_y

        # Check if snake eats food
        if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
            score += 10
            snake_length += 3
            food_x = random.randint(0, 1200 - snake_size)
            food_y = random.randint(0, 500 - snake_size)

        # LENGTH LOGIC
        head = [snake_x, snake_y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # COLLISION LOGIC
        if head in snake_list[:-1]:
            game_over = True

    gameWindow.fill(white)

    if game_over:
        game_over_screen()
    else:
        show_score(score)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        for segment in snake_list:
            pygame.draw.rect(gameWindow, black, [segment[0], segment[1], snake_size, snake_size])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
