import pygame, sys

pygame.init() # Initialize pygame module.
screen = pygame.display.set_mode((1200,600)) # Creates the display (Width,Height)
clock = pygame.time.Clock() # Creates internal Clock for fps/tick system
pygame.display.set_caption("Test Game") # Display Window Title

while True: # Game runs inside of this loop.
    for event in pygame.event.get(): # Loops through all events in pygame module
        if event.type == pygame.QUIT: # Finds event QUIT (X button on window)
            pygame.quit() # Close window
            sys.exit() # Exits Code

    pygame.display.update() # Takes evrything and updates display surface.
    clock.tick(60) # Setting internal clock to 60fps ensuring while loop doesnt run more than 60 times per second.