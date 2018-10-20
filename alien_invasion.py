import sys
import pygame

def run_game():
    #initializes game and creates a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

# Start the main loop of the game
    while True:
        #listen for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(bg_color)
            pygame.display.flip()
run_game()
