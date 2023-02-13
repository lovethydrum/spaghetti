import pygame

pygame.init()

pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
game_window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("English RPG")
game_surface = pygame.Surface((1200, 800))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))

running = True

while running:
    ev = pygame.event.get()
    for event in ev:
        if event == pygame.QUIT:
            running = False