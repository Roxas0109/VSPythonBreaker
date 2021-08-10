import pygame
import os
class Paddle(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, images, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.index = 0
       self.image = pygame.Surface([width, height])
       self.transformed_images = []
       for img in images:
           self.transformed_images.append(pygame.transform.scale(img, (width, height)))
       
       self.image = self.transformed_images[self.index]

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def updateImage(self):
        #print(self.index)
        self.index+=1
        if self.index >= len(self.transformed_images):
            self.index = 0
        self.image = self.transformed_images[self.index]

    def movement(self, keys_pressed, VEL, screen_Width):
        #if specific keys are pressed, do action
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 0: #LEFT
            self.rect.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width < screen_Width: #RIGHT
            self.rect.x += VEL