#ball, paddle, rect,  website: https://www.pygame.org/docs/tut/tom_games4.html

import pygame


#game dimensions x and y axis’
screen_size = 640, 480

#random width for paddle; can be changed
paddle_width = 60
paddle_height = 10
ball_diameter = 16

max_paddle_x = screen_size[0] - paddle_width
max_ball_x = screen_size[0] - ball_diameter
max_ball_y = screen_size[1] - ball_diameter

# paddle y coordinate
paddle_y = screen_size[1] - paddle_height - 10 

#used to start the game and create the environment
def __init__(self):
        pygame.init()        
        self.screen = pygame.display.set_mode(screen_size)




# https://www.pygame.org/docs/ref/rect.html
#used to create in game parameters and basic ball structures, paddle 
#structures, sizes, basic velocity/speeds of the ball(movement), etc.

def init_game(self):
     self.paddle = pygame.Rect(300, paddle_y, paddle_width, paddle_height)
     self.ball = pygame.Rect(300, paddle_y - ball_diameter, ball_diameter, ball_diameter)
    
     self.ball_vel = [-5,5]



#will measure moving the ball x-axis and y-axis plus it will monitor
#speed of the ball - x component of the velocity => 
#https://stackoverflow.com/questions/48776989/how-to-remove-a-rect-in-pygame-
#using-colliderect-only-if-the-rect-has-been-hi

#ball_vel used to show the ball moving from pygame both on the x or y axis or both defined above 

def move_ball (self):
        self.ball.left += self.ball_vel[0]
        self.ball.top += self.ball_vel[1]
    #ball direction x-axis
        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] =- self.ball_vel[0]
        elif self.ball.left >= max_ball_X:
            self.ball.left = max_ball_X
            self.ball_vel[0] =- self.ball_vel[0]
        
        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1] =- self.ball_vel[1]

# https://gamedev.stackexchange.com/questions/61705/pygame-colliderect-but-how-do-they-collide
#goes into depth of the ball.colliderect class part of pygame

def handle_collisions(self):
    for brick in self.bricks:
        if self.ball.colliderect(brick):
            self.score += 3
            self.ball_vel[1] = -self.ball_vel[1]
            self.bricks.remove(brick)
            break
        
    if len(self.bricks) == 0:
        self.state = state_winner
            
    if self.ball.colliderect(self.paddle):
        self.ball.top = paddle_y - ball_diameter
        self.ball_vel[1] =- self.ball_vel[1]
            
        #if the ball hits the ground either delete a life or end game
        #can configure this way later
        #elif self.ball.top > self.paddle.top:
            #self.lives -= 1
            #if self.lives > 0:
            #ball hits paddle and still able to play
            #    self.state = ball_good
            #else:
            #    self.state = game_over

