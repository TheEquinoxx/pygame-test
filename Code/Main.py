import pygame

pygame.init() # Initialize pygame module.
screen = pygame.display.set_mode((1200,600))

while True: # Game runs inside of this loop.
    for event in pygame.event.get(): # Loops through all events in pygame module
        if event.type == pygame.QUIT: # Finds event QUIT (X button on window)
            pygame.quit() # Close window

    pygame.display.update() # Takes evrything and updates display surface.