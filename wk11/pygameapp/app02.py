import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame 01")
clock = pygame.time.Clock() #create a clock object to manage the frame rate
running = True
while running: #game loop
    for event in pygame.event.get(): #event handling
        if event.type == pygame.QUIT: #check for quit event
            running = False
    clock.tick(60) #limit the frame rate to 60 FPS
    screen.fill((255, 255, 255)) #fill the screen with white
    font = pygame.font.SysFont("Arial", 36) #create a font object
    text = font.render(f"{clock.get_fps():.2f}", True, (0, 0, 0))
    screen.blit(text, (300, 230)) #draw the text on the screen
    pygame.display.update() #update the display
pygame.quit()
