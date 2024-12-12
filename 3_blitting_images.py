import pygame 

#init

pygame.init()

# create a display surface and create its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# create images, create an image surface object that return the image on it.


running = True
pygame.display.set_caption("Blitting images")
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


# End of game loop

pygame.quit()