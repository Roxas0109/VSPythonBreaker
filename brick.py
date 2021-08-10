import pygame
import os
class Brick(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,image, broken_img, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image = pygame.transform.scale(image, (width, height))
       self.broken_img = pygame.transform.scale(broken_img, (width, height))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

       #health
       self.health = 2

    def checkHealth(self):
        if self.health == 1:
            self.image = self.broken_img
        elif self.health == 0:
            self.kill()
