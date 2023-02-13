import random
import pygame


pygame.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 350, screen_height - 60
game_window = pygame.display.set_mode((window_width, window_height))
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))
pygame.display.update()

running = True

while running:
    ev = pygame.event.get()
    for event in ev:

    hundreds_digit = random.randint(1, 9)
    tens_digit = random.randint(0, 9)
    ones_digit = random.randint(0, 9)

    three_digit_number = f"  \n\n\n\n\n\n{hundreds_digit}{tens_digit}{ones_digit}"
    print(three_digit_number)
    continue_prompt = input("  \n\n\n\n\nDo you want to continue?  Y/N  : ").lower()
    if continue_prompt == "y" or continue_prompt == "":
        pass
    else:
        running = False
