import pygame
pygame.init()

# generate the window
pygame.display.set_caption("WindowsConnection")
screen = pygame.display.set_mode((180, 150), pygame.NOFRAME)
running = True

# import image background
background = pygame.image.load('assets/bg.jpg')
# While
while running:

    # add background imag
    screen.blit(background, (0, 0))

    # refresh the screen
    pygame.display.flip()

    # if player use this or
    for event in pygame.event.get():
        # event is run don't close
        if event.type == pygame.QUIT:
            running = True
            print("Connect Please")
            print("What?!")