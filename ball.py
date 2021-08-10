import pygame
from random import randint

class Ball(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image, width, height, vel):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image = pygame.transform.scale(image, (width, height))

       #self.velocity = [randint(4,8),randint(-8,8)]
       self.velocity = [vel,randint(4,8)]

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def move_ball(self, screenWidth, screenHeight):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x + self.rect.width >= screenWidth or self.rect.x<=0:
            self.velocity[0] *= -1
        
        if self.rect.y<=0:
            self.velocity[1] *= -1

        if self.rect.y + self.rect.height >= screenHeight:
            self.rect.x = 345
            self.rect.y = 195
            self.velocity = [self.velocity[0],randint(4,8)]
        

    def brick_bounce(self):
        #self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(1,8)

    def paddle_bounce(self):
        #self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,-1)