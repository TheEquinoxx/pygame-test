import pygame, sys

class Game:
    def __init__(self):
        pygame.init() # Initialize pygame module
        self.screen = pygame.display.set_mode((1600,800)) # Creates the display (Width,Height)
        self.clock = pygame.time.Clock() # Creates internal Clock for fps/tick system
        pygame.display.set_caption("Test Game") # Display Window Title

    def run(self):
        while True: # Game runs inside of this loop
            for event in pygame.event.get(): # Loops through all events in pygame module
                if event.type == pygame.QUIT: # Finds event QUIT (X button on window)
                    pygame.quit() # Close window
                    sys.exit() # Exits Code

            self.screen.fill("black")
            pygame.display.update() # Takes evrything and updates display surface
            self.clock.tick(60) # Setting internal clock to 60fps ensuring while loop doesnt run more than 60 times per second

if __name__ == "__main__": # Check if Main file
    game = Game() # Creating instance of Game class
    game.run() # run function from game class instance