import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
sara_sheet = pygame.image.load("sara/sara-cal1.png")
sara_ract = pygame.Rect(0, 0, 34, 56)
sara_pos = pygame.Rect(50, 50, 34, 56)
clock = pygame.time.Clock()
while running: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and sara_pos.x+sara_ract.width < 400:
        sara_pos.x += 5
    elif key[pygame.K_LEFT] and sara_pos.x > 0:
        sara_pos.x -= 5
    elif key[pygame.K_DOWN] and sara_pos.y+sara_ract.height < 300:
        sara_pos.y += 5
    elif key[pygame.K_UP] and sara_pos.y > 0:
        sara_pos.y -= 5
    clock.tick(90) #limit to 60 frames per second
    screen.fill((255, 255, 255)) #fill the screen with white
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0)) #render the text
    screen.blit(sara_sheet, sara_pos, sara_ract) #draw the image on the screen
    screen.blit(text, (300, 230)) #draw the text on the screen
    pygame.display.update() #update the display
pygame.quit()