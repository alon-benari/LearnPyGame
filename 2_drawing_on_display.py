import pygame 

#init

pygame.init()

# create a display surface and create its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #define the display surface
# colors
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
CYAN = (0,255,255)
CYAN1 = (0,255,122)

display_surface.fill(BLUE) # fill the display surface with a certain color

# draw line: display surface, start point, end point thickness
pygame.draw.line(display_surface, RED, (0,0), (100,100), 4)
pygame.draw.line(display_surface,YELLOW , (100,100), (200,300), 4)

# draw circle ( display surface, color, center, radius, thickness, 0 tofill)
pygame.draw.circle(display_surface,WHITE, (WINDOW_WIDTH/2.0, WINDOW_HEIGHT/2.0),100 ,11)

#draw rectangle ( surface, color  (top_x, top_y, width, heigh))
pygame.draw.rect(display_surface,CYAN, (500,0,100,100))
pygame.draw.rect(display_surface,CYAN1, (500,100,100,100))

running = True
pygame.display.set_caption("Hello World")
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # update the display
    pygame.display.update()

# End of game loop

pygame.quit()