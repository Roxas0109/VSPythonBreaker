import pygame
import os
from brick import Brick

#app window size and flags
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Breaker')

#color
BLACK = (0,0,0)

#LOCK FPS
FPS = 60

#CREATE BLOCKS
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30

BLUE_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '01-Breakout-Tiles.png'))
GREEN_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '15-Breakout-Tiles.png'))
RED_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '07-Breakout-Tiles.png'))

def draw_window(blueBlock):
    WIN.fill(BLACK)
    blueBlock.draw(WIN)
    pygame.display.update()

def create_bricks(allBricks):
    for i in range(7):
        brick = Brick(BLUE_BLOCK_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 60
        allBricks.add(brick)
    for i in range(7):
        brick = Brick(GREEN_BLOCK_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 100
        allBricks.add(brick)
    for i in range(7):
        brick = Brick(RED_BLOCK_IMAGE, BLOCK_WIDTH, BLOCK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 140
        allBricks.add(brick)

def main():
    #init blocks
    allBricks = pygame.sprite.Group()
    create_bricks(allBricks)

    #set FPS
    clock = pygame.time.Clock()

    #while true, run game
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(allBricks)
    pygame.quit()

if __name__ == "__main__":
    main()
