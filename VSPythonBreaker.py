import pygame
import os
from brick import Brick
from testball import TestBall

#app window size and flags
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Breaker')

#color
BLACK = (0,0,0)
WHITE = (255,255, 255)


#LOCK FPS
FPS = 60

#CREATE BLOCKS
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30

BLUE_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '01-Breakout-Tiles.png'))
BLUE_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '02-Breakout-Tiles.png'))
GREEN_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '15-Breakout-Tiles.png'))
GREEN_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '16-Breakout-Tiles.png'))
RED_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '07-Breakout-Tiles.png'))
RED_BROKEN_IMAGE = pygame.image.load(os.path.join('Assets', '08-Breakout-Tiles.png'))

def draw_window(brick_Group, test_ball_group):
    WIN.fill(BLACK)
    brick_Group.draw(WIN)
    test_ball_group.draw(WIN)
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

def main():
    #init blocks
    brick_Group = pygame.sprite.Group()
    create_bricks(brick_Group)

    #temp ball
    test_ball_group = pygame.sprite.GroupSingle()
    test_ball = TestBall(WHITE, 30, 30)
    test_ball.rect.x = 400
    test_ball.rect.y = 500
    test_ball_group.add(test_ball)

    #set FPS
    clock = pygame.time.Clock()

    #while true, run game
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #handle movement of test ball
        keys_pressed = pygame.key.get_pressed()
        test_ball.movement(keys_pressed, 8)

        #if ball touches brick, break it
        collisions = pygame.sprite.spritecollide(test_ball, brick_Group, False)

        for brick in collisions:
            if(brick.health == 0):
                brick.kill()
            else:
                brick.health-=1
                brick.checkHealth()
                print(brick.health)

        draw_window(brick_Group, test_ball_group)
    pygame.quit()

if __name__ == "__main__":
    main()
