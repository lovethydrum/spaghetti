# IMPORTED LIBRARIES #
import math
import pygame
import random
import os
import ctypes

# Stop Windows 10 scaling and center the display
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Initialise all the pygame modules
pygame.init()

# Summon the Fish God
uozaki_logo = pygame.image.load("Uozaki_fish.jpg")
# Create game windows
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
# Set the screen for either computer configuration
if screen_width == 1280:
    resize_factor = (2 / 3)
    window_width, window_height = screen_width-373, screen_height - 140
    uozaki_logo = pygame.transform.scale(uozaki_logo, (int(194*resize_factor), int(124*resize_factor)))
else:
    resize_factor = 1
    window_width, window_height = screen_width-560, screen_height-60
game_window = pygame.display.set_mode((window_width, window_height))

# create lists for upper and lower case to draw from
upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]


def upper_answer():
    return upper_case[random.randint(0, (len(upper_case) - 1))]


def lower_answer():
    return lower_case[random.randint(0, (len(lower_case) - 1))]


class AnswerCreator:
    def __init__(self):
        self.answer_text = "A"
        self.case = "upper"
        self.x = 205*resize_factor
        self.y = 130*resize_factor
        self.randomize_answer()

    def randomize_answer(self):
        if self.case == "upper":
            self.x, self.y = 205*resize_factor, 230*resize_factor
            self.answer_text = upper_answer()
        elif self.case == "lower":
            self.answer_text = lower_answer()
            self.x, self.y = 265*resize_factor, 260*resize_factor

    def display_answer(self):
        # game_window.blit(font1.render(answer.answer_text, True, (0, 0, 0), ), (self.x, self.y))
        display_answer = font1.render(answer.answer_text, True, (0, 0, 0), )
        if self.case == "upper":
            display_answer_rect = display_answer.get_rect(center=(485*resize_factor, 580*resize_factor))
            game_window.blit(display_answer, display_answer_rect)
        elif self.case == "lower":
            display_answer_rect = display_answer.get_rect(center=(485*resize_factor, 530*resize_factor))
            game_window.blit(display_answer, display_answer_rect)


answer = AnswerCreator()

running = True


# Previous was 600, 510   - Current is 1.5x original
CLICKABLE_WINDOW_LENGTH = 900*resize_factor
CLICKABLE_WINDOW_HEIGHT = 765*resize_factor
CLICKABLE_WINDOW_X = 55*resize_factor
CLICKABLE_WINDOW_Y = 180*resize_factor

darkness_window = pygame.Surface((CLICKABLE_WINDOW_LENGTH, CLICKABLE_WINDOW_HEIGHT))
whiteness_window = pygame.Surface((CLICKABLE_WINDOW_LENGTH, CLICKABLE_WINDOW_HEIGHT))

# Set Caption
pygame.display.set_caption('Flashlight Game')

# Font
font1 = pygame.font.Font('MitsuEHandwriting-R.otf', int(550*resize_factor))
font2 = pygame.font.Font('MitsuEHandwriting-R.otf', int(18*resize_factor))
font3 = pygame.font.Font('MitsuEHandwriting-R.otf', int(350*resize_factor))
flashlight_font = pygame.font.Font('MitsuEHandwriting-R.otf', int(30*resize_factor))
button_font = pygame.font.Font('MitsuEHandwriting-R.otf', int(40*resize_factor))

# Fill the windows with color
game_window.fill((255, 255, 255))
darkness_window.fill((0, 0, 0))
whiteness_window.fill((255, 255, 255))

# Clean window to keep the sides from disappearing

clickable_space = pygame.draw.rect(game_window, (255, 0, 0), (CLICKABLE_WINDOW_X, CLICKABLE_WINDOW_Y,
                                                              CLICKABLE_WINDOW_LENGTH, CLICKABLE_WINDOW_HEIGHT))


# Draw darkness
def draw_darkness():
    game_window.blit(darkness_window, (CLICKABLE_WINDOW_X, CLICKABLE_WINDOW_Y))


# Button Creation
class Buttons(pygame.rect.Rect):
    def __init__(self, color, x, y, width, height, text, text_x, text_y, hover_color, clicked_color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_x = text_x
        self.text_y = text_y
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.hover = False
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        if not self.hover:
            pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
            game_window.blit(button_font.render(self.text, True, (0, 0, 0), ), (self.text_x, self.text_y))
        elif self.hover:
            if self.clicked:
                pygame.draw.rect(game_window, self.clicked_color, (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(game_window, self.hover_color, (self.x, self.y, self.width, self.height))
            game_window.blit(button_font.render(self.text, True, (0, 0, 0), ), (self.text_x, self.text_y))
        pygame.draw.rect(game_window, (0, 0, 0), (self.x, self.y, self.width, self.height), 5)


class CircleButton:
    def __init__(self, x, y, radius, text, text_x, text_y):
        self.color = (169, 169, 169)
        self.selected_color = (255, 230, 0)
        self.x = x
        self.y = y
        self.text = text
        self.text_x = text_x
        self.text_y = text_y
        self.radius = radius
        self.selected = False

    def draw_button(self):
        if self.selected:
            pygame.draw.circle(game_window, (0, 0, 0), (self.x, self.y), self.radius+5, 7)
            pygame.draw.circle(game_window, self.selected_color, (self.x, self.y), self.radius, 0)
            game_window.blit(flashlight_font.render(self.text, True, (0, 0, 0), ), (self.text_x, self.text_y))
        else:
            pygame.draw.circle(game_window, self.color, (self.x, self.y), self.radius, 0)
            game_window.blit(flashlight_font.render(self.text, True, (0, 0, 0), ), (self.text_x, self.text_y))

    def collidepoint(self, mouse_position):
        x1, y1 = mouse_position
        distance = math.hypot(x1 - self.x, y1 - self.y)
        if distance <= self.radius:
            return True


big_flashlight_button = CircleButton(x=1145*resize_factor, y=310*resize_factor, radius=120*resize_factor, text="Big",
                                     text_x=1120*resize_factor, text_y=290*resize_factor)
med_flashlight_button = CircleButton(x=1145*resize_factor, y=540*resize_factor, radius=90*resize_factor, text="Medium",
                                     text_x=1085*resize_factor, text_y=515*resize_factor)
lil_flashlight_button = CircleButton(x=1145*resize_factor, y=710*resize_factor, radius=60*resize_factor, text="Small",
                                     text_x=1105*resize_factor, text_y=690*resize_factor)
reveal_button = Buttons(color=(255, 94, 19), x=985*resize_factor, y=795*resize_factor, width=320*resize_factor,
                        height=150*resize_factor, text="Answer", text_x=1065*resize_factor,
                        text_y=840*resize_factor, hover_color=(255, 144, 39), clicked_color=(255, 50, 19))
upper_case_button = Buttons(color=(137, 209, 254), x=55*resize_factor, y=60*resize_factor, width=250*resize_factor,
                            height=100*resize_factor, text="ABC", text_x=125*resize_factor, text_y=80*resize_factor,
                            hover_color=(167, 239, 255), clicked_color=(0, 0, 255))
lower_case_button = Buttons(color=(137, 209, 254), x=725*resize_factor, y=60*resize_factor, width=230*resize_factor,
                            height=100*resize_factor, text="abc", text_x=805*resize_factor, text_y=80*resize_factor,
                            hover_color=(167, 239, 255), clicked_color=(0, 0, 255))

button_list = [reveal_button, big_flashlight_button, med_flashlight_button,
               lil_flashlight_button, upper_case_button, lower_case_button]

flashlight_size = 120*resize_factor


# Flashlight function
def flashlight_loadout():
    global flashlight_size
    global big_flashlight_button
    global med_flashlight_button
    global lil_flashlight_button
    if flashlight_state == 1:
        flashlight_size = 120*resize_factor
        big_flashlight_button.selected = True
        med_flashlight_button.selected = False
        lil_flashlight_button.selected = False
    elif flashlight_state == 2:
        flashlight_size = 90*resize_factor
        big_flashlight_button.selected = False
        med_flashlight_button.selected = True
        lil_flashlight_button.selected = False
    elif flashlight_state == 3:
        flashlight_size = 60*resize_factor
        big_flashlight_button.selected = False
        med_flashlight_button.selected = False
        lil_flashlight_button.selected = True


def draw_all_buttons():
    game_window.blit(whiteness_window, (975*resize_factor, 100*resize_factor))
    game_window.blit(uozaki_logo, (405*resize_factor, 40*resize_factor))
    flashlight_loadout()
    for button in button_list:
        button.draw_button()


flashlight_state = 1
draw_all_buttons()

# Update display
pygame.display.update()
# Game loop
dragging = False
game_running = True
while game_running:
    ev = pygame.event.get()
    pos = pygame.mouse.get_pos()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reveal_button.collidepoint(event.pos):
                reveal_button.clicked = True
                draw_all_buttons()
                game_window.blit(whiteness_window, (CLICKABLE_WINDOW_X, CLICKABLE_WINDOW_Y))
                answer.display_answer()
            elif big_flashlight_button.collidepoint(event.pos):
                flashlight_state = 1
                draw_all_buttons()
            elif med_flashlight_button.collidepoint(event.pos):
                flashlight_state = 2
                draw_all_buttons()
            elif lil_flashlight_button.collidepoint(event.pos):
                flashlight_state = 3
                draw_all_buttons()
            elif upper_case_button.rect.collidepoint(event.pos):
                answer.case = "upper"
                upper_case_button.clicked = True
                draw_all_buttons()
                answer.randomize_answer()
                answer.display_answer()
                draw_darkness()
                pygame.display.update()
            elif lower_case_button.rect.collidepoint(event.pos):
                answer.case = "lower"
                lower_case_button.clicked = True
                draw_all_buttons()
                answer.randomize_answer()
                answer.display_answer()
                draw_darkness()
                pygame.display.update()
            elif clickable_space.collidepoint(event.pos):
                flashlight = pygame.draw.circle(game_window, (255, 255, 255), pos, flashlight_size, 0)
                dragging = True
                answer.display_answer()
                draw_all_buttons()
                pygame.display.update()
        elif upper_case_button.rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONUP:
                upper_case_button.clicked = False
            upper_case_button.hover = True
            draw_all_buttons()
            pygame.display.update()
        elif lower_case_button.rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONUP:
                lower_case_button.clicked = False
            lower_case_button.hover = True
            draw_all_buttons()
            pygame.display.update()
        elif reveal_button.rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONUP:
                reveal_button.clicked = False
                draw_darkness()
            reveal_button.hover = True
            draw_all_buttons()
            pygame.display.update()
        elif dragging:
            draw_darkness()
            flashlight = pygame.draw.circle(game_window, (255, 255, 255), pos, flashlight_size, 0)
            draw_all_buttons()
            answer.display_answer()
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                draw_darkness()
                dragging = False
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            reveal_button.clicked = False
            for buttons in button_list:
                buttons.clicked = False
            draw_darkness()
            pygame.display.update()
        elif event.type == pygame.QUIT:
            game_running = False
        else:
            for buttons in button_list:
                buttons.hover = False
            reveal_button.clicked = False
            draw_all_buttons()
            draw_darkness()
        pygame.display.update()
