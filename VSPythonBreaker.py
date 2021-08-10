import pygame
import os
from brick import Brick
from paddle import Paddle
from ball import Ball
pygame.font.init()

#app window size and flags
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Breaker')

#color
BLACK = (0,0,0)
WHITE = (255,255, 255)

#FONT 
TEXT_FONT = pygame.font.SysFont('comicsans', 40)


#LOCK FPS
FPS = 30
VELOCITY = 10

#CREATE BLOCKS
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30

BLUE_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '01-Breakout-Tiles.png'))
BLUE_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '02-Breakout-Tiles.png'))
GREEN_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '15-Breakout-Tiles.png'))
GREEN_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '16-Breakout-Tiles.png'))
RED_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '07-Breakout-Tiles.png'))
RED_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '08-Breakout-Tiles.png'))

#CREATE PADDLE
PADDLE_WIDTH, PADDLE_HEIGHT = 80 , 30

PADDLE_IMAGES = []
PADDLE_IMAGES.append(pygame.image.load(os.path.join('Assets', '50-Breakout-Tiles.png')))
PADDLE_IMAGES.append(pygame.image.load(os.path.join('Assets', '51-Breakout-Tiles.png')))
PADDLE_IMAGES.append(pygame.image.load(os.path.join('Assets', '52-Breakout-Tiles.png')))

#BALL
BALL_WIDTH, BALL_HEIGHT = 40, 40

BALL_IMAGE = pygame.image.load(os.path.join('Assets', '58-Breakout-Tiles.png'))

#draw objects on screen
def draw_window(sprite_Group, GAME_TEXT, EXIT_TEXT):
    SCREEN.fill(BLACK)
    sprite_Group.draw(SCREEN)
    SCREEN.blit(EXIT_TEXT, (0, EXIT_TEXT.get_height()))
    SCREEN.blit(GAME_TEXT, (WIDTH - GAME_TEXT.get_width(), GAME_TEXT.get_height()))
    pygame.display.update()

def create_bricks(brick_Group):
    for i in range(7):
        brick = Brick(BLUE_BLOCK_IMAGE, BLUE_BROKEN_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 60
        brick_Group.add(brick)
    for i in range(7):
        brick = Brick(GREEN_BLOCK_IMAGE, GREEN_BROKEN_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 100
        brick_Group.add(brick)
    for i in range(7):
        brick = Brick(RED_BLOCK_IMAGE, RED_BROKEN_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 140
        brick_Group.add(brick)

def display_timer(timer):
    SCREEN.fill(BLACK)
    draw_text = TEXT_FONT.render(str(timer), 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

def level_finished():
    draw_text = TEXT_FONT.render("FINISHED", 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def game_over():
    draw_text = TEXT_FONT.render("GAME OVER", 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    #init score and lives
    score = 0
    lives = 2
    timer = 3

    #init blocks
    brick_Group = pygame.sprite.Group()
    create_bricks(brick_Group)

    #init paddle
    paddle_Group = pygame.sprite.GroupSingle()
    paddle = Paddle(PADDLE_IMAGES, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle.rect.x = 400
    paddle.rect.y = 500
    paddle_Group.add(paddle)

    #init ball
    ball_Group = pygame.sprite.GroupSingle()
    ball = Ball(BALL_IMAGE, BALL_WIDTH, BALL_HEIGHT)
    ball.rect.x = 345
    ball.rect.y = 195
    ball_Group.add(ball)

    #group to hold all sprites
    sprite_Group = pygame.sprite.Group()
    sprite_Group.add(brick_Group, paddle_Group, ball_Group)

    #set FPS
    clock = pygame.time.Clock()

    #display timer before game starts
    while timer > 0:
        display_timer(timer)
        timer -= 1

    #while true, run game
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #handle movement of ball and paddle
        keys_pressed = pygame.key.get_pressed()
        paddle.movement(keys_pressed, VELOCITY, WIDTH)

        #to quit game
        if keys_pressed[pygame.K_x]:
            run = False
            pygame.quit()

        ball.move_ball(WIDTH, HEIGHT)

        #check if ball hits the walls
        if ball.rect.x + ball.rect.width >= WIDTH or ball.rect.x<=0:
            ball.velocity[0] *= -1
        
        if ball.rect.y<=0:
            ball.velocity[1] *= -1

        if ball.rect.y + ball.rect.height >= HEIGHT:
            lives -= 1
            if lives < 0:
                game_over()
                break
            ball.rect.x = 345
            ball.rect.y = 195

        #if ball touches brick, break it
        brick_collision = pygame.sprite.spritecollide(ball, brick_Group, False)

        for brick in brick_collision:
            brick.health -= 1
            score = brick.checkHealth(score)
            ball.brick_bounce()

        #paddle collision
        paddle_collision = pygame.sprite.spritecollide(ball, paddle_Group, False)

        for paddle in paddle_collision:
            ball.paddle_bounce()

        #check if all bricks are gone
        if not brick_Group:
            level_finished()
            break

        #update window
        GAME_TEXT = TEXT_FONT.render("Lives: "+ str(lives) +" Score: " + str(score), 1, WHITE)
        EXIT_TEXT = TEXT_FONT.render("Press 'x' to exit game", 1, WHITE)
        paddle.updateImage()
        draw_window(sprite_Group, GAME_TEXT, EXIT_TEXT)
    main()

if __name__ == "__main__":
    main()
