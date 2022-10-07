import pygame

# SPREAD CHECKPOINTS RANDOMLY ACROSS ENVIRONMENT - THEY WILL BE REWARD + 10

class Checkpoint:
    def __init__(self, screen, x, y):
        # same dimensions for all robots
        self.width, self.height = 40, 40
        self.x, self.y = x, y
        self.screen = screen
        self.color = (0,255,0)
        self.rect = pygame.draw.rect(self.screen, self.color, (0,0,self.width,self.height))

        # integrate position randomizer with main 


    def draw(self):
        self.robot = pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height))
    
        