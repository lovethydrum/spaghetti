# IMPORTED LIBRARIES #
import pygame
import sys
import random
import os

upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]

hover = False
clicked = False
flashlight_state = 1

def upper_answer():
    return upper_case[random.randint(0, (len(upper_case) - 1))]


def lower_answer():
    return lower_case[random.randint(0, (len(lower_case) - 1))]

class Buttons:
    def __init__(self, color, x, y, width, height, hover_color, clicked_color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.hover = False
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self, surface):
        if not hover:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        elif hover:
            if clicked:
                pygame.draw.rect(surface, self.clicked_color, (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(surface, self.hover_color, (self.x, self.y, self.width, self.height))


answer = upper_answer()
running = True

os.environ['SDL_VIDEO_CENTERED'] = '1'
# Initialise all the pygame modules
pygame.init()

# Create game windows
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width-200, screen_height-50
game_window = pygame.display.set_mode((window_width, window_height))

darkness_window = pygame.Surface((600, 510))
whiteness_window = pygame.Surface((600, 510))

# Set Caption
pygame.display.set_caption('Uozaki Flashlight Game')

# Font
font1 = pygame.font.SysFont('MitsuEHandwriting R', 500)
font2 = pygame.font.SysFont('MitsuEHandwriting R', 18)
font3 = pygame.font.SysFont('MitsuEHandwriting R', 350)
answer_font = pygame.font.SysFont('MitsuEHandwriting R', 40)
text1 = font1.render(answer, True, (0, 0, 0),)
# Fill the windows with color
game_window.fill((255, 255, 255))
darkness_window.fill((0, 0, 0))
whiteness_window.fill((255, 255, 255))

# Clean window to keep the sides from disappearing

clickable_space = pygame.draw.rect(game_window, (255, 0, 0), (130, 95, 600, 510))

# Draw text and darkness

game_window.blit(text1, (190, -30))
game_window.blit(darkness_window, (130, 95))

# Button Creation
flashlight_size = 100
flashlight_color_on = (255, 230, 0)
flashlight_color_off = (169, 169, 169)

filled = 0

reveal_button = pygame.draw.rect(game_window, [255, 94, 19], [800, 505, 205, 100], filled)
reveal_button_text = answer_font.render("Answer", True, (0, 0, 0),)
game_window.blit(reveal_button_text, (830, 530))

big_flashlight_button = pygame.draw.circle(game_window, flashlight_color_on, (900, 90), 80, 0)
big_flashlight_text = font2.render("Big", True, (0, 0, 0),)
game_window.blit(big_flashlight_text, (885, 80))

med_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (901, 240), 65, 0)
med_flashlight_text = font2.render("Medium", True, (0, 0, 0),)
game_window.blit(med_flashlight_text, (865, 228))

lil_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (902, 360), 50, filled)
lil_flashlight_text = font2.render("Small", True, (0, 0, 0),)
game_window.blit(lil_flashlight_text, (875, 350))

upper_case_button = Buttons((137, 209, 254), 130, 10, 140, 80, (167, 239, 255), (0, 0, 255))
upper_case_button.draw_button(game_window)
upper_case_button_text = answer_font.render("ABC", True, (0, 0, 0),)
game_window.blit(upper_case_button_text, (148, 25))

lower_case_button = Buttons((137, 209, 254), 350, 10, 140, 80, (167, 239, 255), (107, 179, 224))
lower_case_button.draw_button(game_window)
lower_case_button_text = answer_font.render("abc", True, (0, 0, 0),)
game_window.blit(lower_case_button_text, (378, 25))

# Flashlight function
def flashlight_loadout():
    if flashlight_state == 1:
        big_flashlight_button = pygame.draw.circle(game_window, flashlight_color_on, (900, 90), 80, 0)
        big_flashlight_text = font2.render("Big", True, (0, 0, 0), )
        game_window.blit(big_flashlight_text, (885, 80))
        med_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (901, 240), 65, 0)
        med_flashlight_text = font2.render("Medium", True, (0, 0, 0), )
        game_window.blit(med_flashlight_text, (865, 228))
        lil_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (902, 360), 50, filled)
        lil_flashlight_text = font2.render("Small", True, (0, 0, 0), )
        game_window.blit(lil_flashlight_text, (875, 350))
    elif flashlight_state == 2:
        big_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (900, 90), 80, 0)
        big_flashlight_text = font2.render("Big", True, (0, 0, 0), )
        game_window.blit(big_flashlight_text, (885, 80))
        med_flashlight_button = pygame.draw.circle(game_window, flashlight_color_on, (901, 240), 65, 0)
        med_flashlight_text = font2.render("Medium", True, (0, 0, 0), )
        game_window.blit(med_flashlight_text, (865, 228))
        lil_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (902, 360), 50, filled)
        lil_flashlight_text = font2.render("Small", True, (0, 0, 0), )
        game_window.blit(lil_flashlight_text, (875, 350))
    elif flashlight_state == 3:
        big_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (900, 90), 80, 0)
        big_flashlight_text = font2.render("Big", True, (0, 0, 0), )
        game_window.blit(big_flashlight_text, (885, 80))
        med_flashlight_button = pygame.draw.circle(game_window, flashlight_color_off, (901, 240), 65, 0)
        med_flashlight_text = font2.render("Medium", True, (0, 0, 0), )
        game_window.blit(med_flashlight_text, (865, 228))
        lil_flashlight_button = pygame.draw.circle(game_window, flashlight_color_on, (902, 360), 50, filled)
        lil_flashlight_text = font2.render("Small", True, (0, 0, 0), )
        game_window.blit(lil_flashlight_text, (875, 350))
# Size and location variables to alter in the loop
answer_location_x = 190
answer_location_y = -30
# Update our display
pygame.display.update()
# Game loop
dragging = False
game_running = True
while game_running:
    # Loop through all active events
    ev = pygame.event.get()
    pos = pygame.mouse.get_pos()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reveal_button.collidepoint(event.pos):
                game_window.blit(whiteness_window, (130, 95))
                game_window.blit(text1, (answer_location_x, answer_location_y))
                pygame.display.update()
            elif big_flashlight_button.collidepoint(event.pos):
                flashlight_size = 100
                flashlight_state = 1
                flashlight_loadout()
            elif med_flashlight_button.collidepoint(event.pos):
                flashlight_size = 75
                flashlight_state = 2
                flashlight_loadout()
            elif lil_flashlight_button.collidepoint(event.pos):
                flashlight_size = 50
                flashlight_state = 3
                flashlight_loadout()
            elif upper_case_button.rect.collidepoint(event.pos):
                clicked = True
                upper_case_button.draw_button(game_window)
                game_window.blit(upper_case_button_text, (148, 25))
                answer = upper_answer()
                text1 = font1.render(answer, True, (0, 0, 0),)
                answer_location_x, answer_location_y = 190, -30
                game_window.blit(text1, (answer_location_x, answer_location_y))
                game_window.blit(darkness_window, (130, 95))
                clicked = False
                pygame.display.update()
            elif lower_case_button.rect.collidepoint(event.pos):
                clicked = True
                lower_case_button.draw_button(game_window)
                game_window.blit(lower_case_button_text, (378, 25))
                answer = lower_answer()
                text1 = font3.render(answer, True, (0, 0, 0), )
                answer_location_x, answer_location_y = 340, 60
                game_window.blit(text1, (answer_location_x, answer_location_y))
                game_window.blit(darkness_window, (130, 95))
                clicked = False
                pygame.display.update()
            elif clickable_space.collidepoint(event.pos):
                flashlight = pygame.draw.circle(game_window, (255, 255, 255), pos, flashlight_size, 0)
                dragging = True
                game_window.blit(text1, (answer_location_x, answer_location_y))
                upper_case_button.draw_button(game_window)
                game_window.blit(upper_case_button_text, (148, 25))
                lower_case_button.draw_button(game_window)
                game_window.blit(lower_case_button_text, (378, 25))
                flashlight_loadout()
                reveal_button = pygame.draw.rect(game_window, [255, 94, 19], [800, 505, 205, 100], filled)
                reveal_button_text = answer_font.render("Answer", True, (0, 0, 0), )
                game_window.blit(reveal_button_text, (830, 530))
                pygame.display.update()
        elif upper_case_button.rect.collidepoint(pos):
            hover = True
            upper_case_button.draw_button(game_window)
            game_window.blit(upper_case_button_text, (148, 25))
            pygame.display.update()
        elif lower_case_button.rect.collidepoint(pos):
            hover = True
            lower_case_button.draw_button(game_window)
            game_window.blit(lower_case_button_text, (378, 25))
            pygame.display.update()
        elif dragging:
            hover = False
            clicked = False
            game_window.blit(darkness_window, (130, 95))
            flashlight = pygame.draw.circle(game_window, (255, 255, 255), pos, flashlight_size, 0)

            reveal_button = pygame.draw.rect(game_window, [255, 94, 19], [800, 505, 205, 100], filled)
            reveal_button_text = answer_font.render("Answer", True, (0, 0, 0), )
            game_window.blit(reveal_button_text, (830, 530))

            flashlight_loadout()

            upper_case_button.draw_button(game_window)
            game_window.blit(upper_case_button_text, (148, 25))

            lower_case_button.draw_button(game_window)
            game_window.blit(lower_case_button_text, (378, 25))
            game_window.blit(text1, (answer_location_x, answer_location_y))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                game_window.blit(darkness_window, (130, 95))
                dragging = False
                clicked = False
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            game_window.blit(darkness_window, (130, 95))
            dragging = False
            clicked = False
            pygame.display.update()
        elif event.type == pygame.QUIT:
            game_running = False
        else:
            hover = False
            clicked = False
            upper_case_button.draw_button(game_window)
            game_window.blit(upper_case_button_text, (148, 25))
            lower_case_button.draw_button(game_window)
            game_window.blit(lower_case_button_text, (378, 25))
            pygame.display.update()




