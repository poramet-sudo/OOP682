import sys, os
import pygame
from chars.sara import Hero
class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        self.screen_width = 400
        self.screen_height = 300
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = 'Sara Adventure'
        pygame.display.set_caption(self.caption)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, 'sara', 'sara-cal1.png')
        self.hero = Hero('Sara', image_path, 50, 50)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.speed = 5
    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.hero.rect.x > 0:
            self.hero.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.hero.rect.x + self.hero.rect.width < self.screen_width:
            self.hero.rect.x += self.speed
        if keys[pygame.K_UP] and self.hero.rect.y > 0:
            self.hero.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.hero.rect.y + self.hero.rect.height < self.screen_height:
            self.hero.rect.y += self.speed
    def draw_text(self, text_str, position, color=(0, 0, 0)):
        text = self.font.render(text_str, True, color)
        self.screen.blit(text, position)
    def start(self):
        while True:
            elapsed_time = self.clock.tick(60)
            self.handle_close()
            self.handle_movement()
            self.screen.fill((255, 255, 255))
            self.draw_text("Sara Adventure", (100, 100))
            self.hero.update(elapsed_time)
            self.hero.draw(self.screen)
            pygame.display.flip()
if __name__ == "__main__":
    game = SaraAdventure()
    game.start()