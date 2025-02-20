import pygame

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface() # Get display surface

        self.visible_sprites = pygame.sprite.Group() # Creating Group for visible sprites
        self.obstacle_sprites = pygame.sprite.Group()# Creating Group for invisible sprites

    def run(self):
        pass