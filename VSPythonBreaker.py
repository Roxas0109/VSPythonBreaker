import pygame
import os

#app window size and flags
flags = pygame.RESIZABLE
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags)
pygame.display.set_caption('Python Breaker')

#color
BLACK = (0,0,0)

#LOCK FPS
FPS = 60

#CREATE BLOCKS
BLOCK_WIDTH, BLOCK_HEIGHT = 100, 50

BLUE_BLOCK_IMAGE = pygame.image.load(os.path.join('Assets', '01-Breakout-Tiles.png'))
BLUE_BLOCK = pygame.transform.scale(BLUE_BLOCK_IMAGE, (BLOCK_WIDTH, BLOCK_HEIGHT))

def draw_window(blueBlock):
    WIN.fill(BLACK)
    #pygame.draw.rect(WIN, BLACK, blueBlock)
    WIN.blit(BLUE_BLOCK,(blueBlock.x,blueBlock.y))
    WIN.blit(BLUE_BLOCK,(250,300))
    WIN.blit(BLUE_BLOCK,(400,300))
    pygame.display.update()

def main():
    #init blocks objects for images
    blueBlock = pygame.Rect(100,300, BLOCK_WIDTH, BLOCK_HEIGHT)

    #set FPS
    clock = pygame.time.Clock()

    #while true, run game
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(blueBlock)
    pygame.quit()
if __name__ == "__main__":
    main()
