import pygame
import os
from brick import Brick
from testball import TestBall
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
BALL_DIAMETER = 16
BALL_WIDTH, BALL_HEIGHT = 40, 40

BALL_IMAGE = pygame.image.load(os.path.join('Assets', '58-Breakout-Tiles.png'))

def draw_window(sprite_Group):
    SCREEN.fill(BLACK)
    sprite_Group.draw(SCREEN)
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

def level_finished():
    draw_text = TEXT_FONT.render("Finished!", 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
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
    ball = Ball(BALL_IMAGE, BALL_WIDTH, BALL_HEIGHT, VELOCITY)
    ball.rect.x = 345
    ball.rect.y = 195
    ball_Group.add(ball)

    #group to hold all sprites
    sprite_Group = pygame.sprite.Group()
    sprite_Group.add(brick_Group, paddle_Group, ball_Group)


    #temp ball
    test_ball_group = pygame.sprite.GroupSingle()
    test_ball = TestBall(WHITE, 30, 30)
    test_ball.rect.x = 400
    test_ball.rect.y = 500
    test_ball_group.add(test_ball)

    #sprite_Group.add(brick_Group, paddle_Group, test_ball_group)

    #set FPS
    clock = pygame.time.Clock()

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

        ball.move_ball(WIDTH, HEIGHT)

        #if ball touches brick, break it
        brick_collision = pygame.sprite.spritecollide(ball, brick_Group, False)

        for brick in brick_collision:
            brick.health-=1
            brick.checkHealth()
            ball.brick_bounce()
            #print(brick.health)

        paddle_collision = pygame.sprite.spritecollide(ball, paddle_Group, False)

        for paddle in paddle_collision:
            ball.paddle_bounce()

        #check if all bricks are gone
        if not brick_Group:
            print("finished")
            level_finished()
            break

        paddle.updateImage()
        draw_window(sprite_Group)
    main()

if __name__ == "__main__":
    main()
