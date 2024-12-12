import pygame 

#init

pygame.init()

# create a display surface and create its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
pygame.display.set_caption("Hello World")
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


# End of game loop

pygame.quit()