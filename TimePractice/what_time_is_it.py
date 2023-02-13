import pygame
import sys
import os
import random
import ctypes


# This is needed for converting to an exe
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Constants
# LIGHT_GREEN = (208, 240, 192)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# # GREEN = (44, 180, 44)
# # Variables
# score = 0
# high_score = 0
# # Center the screen
# ctypes.windll.user32.SetProcessDPIAware()
# os.environ['SDL_VIDEO_CENTERED'] = '1'
#
# # Initialize PYGAME
# pygame.init()
# # pygame.mixer.init()
#
# # Window setup
# screen_width, screen_height = 1180, 710
# game_window = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("What time is it?")
# game_surface = pygame.Surface((1200, 750))
# game_surface.fill(LIGHT_GREEN)
# game_window.blit(game_surface, (0, 0))

# Import Pictures
# cross = pygame.image.load(resource_path("cross.png"))
# check = pygame.image.load(resource_path("check.png"))
# bath = pygame.image.load(resource_path("bath.png"))
# bed = pygame.image.load(resource_path("bed.png"))
# breakfast = pygame.image.load(resource_path("breakfast.png"))
# dinner = pygame.image.load(resource_path("dinner.png"))
# dream = pygame.image.load(resource_path("dream.png"))
# homework = pygame.image.load(resource_path("homework.png"))
# lunch = pygame.image.load(resource_path("lunch.png"))
# snack = pygame.image.load(resource_path("snack.png"))
# study = pygame.image.load(resource_path("study.png"))
# wake_up = pygame.image.load(resource_path("wake_up.png"))
# stopwatch_raw = pygame.image.load(resource_path("stopwatch.png"))
# stopwatch = pygame.transform.scale(stopwatch_raw, (100, 100))
# end_banner_raw = pygame.image.load(resource_path("end_banner.png"))
# end_banner = pygame.transform.scale(end_banner_raw, (1100, 400))
# pic_list = [bath, bed, breakfast, dinner, dream, homework, lunch, snack, study, wake_up]
# random.shuffle(pic_list)

# Import Audio
# correct_sound = pygame.mixer.Sound(resource_path("correct_sound.ogg"))
# wrong_sound = pygame.mixer.Sound(resource_path("wrong_sound.ogg"))
# countdown_sound = pygame.mixer.Sound(resource_path("countdown.ogg"))
#
# bath_audio = pygame.mixer.Sound(resource_path("bath.ogg"))
# bed_audio = pygame.mixer.Sound(resource_path("bed.ogg"))
# breakfast_audio = pygame.mixer.Sound(resource_path("breakfast.ogg"))
# dinner_audio = pygame.mixer.Sound(resource_path("dinner.ogg"))
# dream_audio = pygame.mixer.Sound(resource_path("dream.ogg"))
# homework_audio = pygame.mixer.Sound(resource_path("homework.ogg"))
# lunch_audio = pygame.mixer.Sound(resource_path("lunch.ogg"))
# snack_audio = pygame.mixer.Sound(resource_path("snack.ogg"))
# study_audio = pygame.mixer.Sound(resource_path("study.ogg"))
# wake_up_audio = pygame.mixer.Sound(resource_path("wake_up.ogg"))
# what_time_audio_dictionary = {
#     "bath": bath_audio,
#     "bed": bed_audio,
#     "breakfast": breakfast_audio,
#     "dinner": dinner_audio,
#     "dream": dream_audio,
#     "homework": homework_audio,
#     "lunch": lunch_audio,
#     "snack": snack_audio,
#     "study": study_audio,
#     "wake_up": wake_up_audio,
#     "": wake_up_audio
# }
#
# audio_list = ["bath", "bed", "breakfast", "dinner", "dream", "homework", "lunch", "snack", "study", "wake_up"]

# # Font
# timer_font = pygame.font.Font(None, 70)
# menu_font = pygame.font.Font(None, 150)
# transition_font = pygame.font.Font(None, 500)
# end_score_font = pygame.font.Font(None, 125)

# Clock
clock = pygame.time.Clock()
counter, text = 60, "60".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
clock_text = str(counter).rjust(3)

#
# class WhatTimeButton:
#     def __init__(self, x, y, pic):
#         self.pic = pic
#         if self.pic == bath:
#             self.name = "bath"
#         elif self.pic == bed:
#             self.name = "bed"
#         elif self.pic == breakfast:
#             self.name = "breakfast"
#         elif self.pic == dinner:
#             self.name = "dinner"
#         elif self.pic == dream:
#             self.name = "dream"
#         elif self.pic == homework:
#             self.name = "homework"
#         elif self.pic == lunch:
#             self.name = "lunch"
#         elif self.pic == snack:
#             self.name = "snack"
#         elif self.pic == study:
#             self.name = "study"
#         elif self.pic == wake_up:
#             self.name = "wake_up"
#         self.width = self.pic.get_width()
#         self.height = self.pic.get_height()
#         self.x = x + ((255 - self.width)/2)
#         self.y = y + ((165 - self.height)/2)
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#
#     def draw_button(self):
#         game_window.blit(self.pic, (self.x, self.y), )
#         pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
#

# This Can Be Preserved
# class MenuButton:
#     def __init__(self, x, y, color):
#         self.width = 400
#         self.height = 250
#         self.x = x
#         self.y = y
#         self.color = color
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#
#     def draw_button(self):
#         pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height), )
#         pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
#

# This just needs to be altered for x/y positions
# class Timer:
#     def __init__(self):
#         self.x = 540
#         self.y = 275
#         self.width = stopwatch.get_width()
#         self.height = stopwatch.get_height()
#
#     def draw_timer(self):
#         clock_text = str(counter).rjust(3)
#         game_window.blit(stopwatch, (self.x, self.y), )
#         pygame.draw.rect(game_window, LIGHT_GREEN, (self.x + 20, self.y + 29, 58, 52))
#         game_window.blit(timer_font.render(clock_text, True, (0, 0, 0)), (self.x + 8, self.y + 33))
# class Timer:
#     def __init__(self):
#         self.x = 540
#         self.y = 50
#         self.color = LIGHT_GREEN
#         self.width = stopwatch.get_width()
#         self.height = stopwatch.get_height()
#
#     def draw_timer(self):
#         timer_text = str(counter).rjust(3)
#         game_window.blit(stopwatch, (self.x, self.y), )
#         pygame.draw.rect(game_window, self.color, (self.x + 20, self.y + 29, 58, 52))
#         game_window.blit(timer_font.render(timer_text, True, (0, 0, 0)), (self.x + 8, self.y + 33))
#         pygame.display.update()
#
#
# # This Can Be Preserved
# class Menu:
#     def __init__(self):
#         self.score_text = 0
#         self.high_score_text = 0
#
#
# what_time_timer = Timer()
# what_time_timer.y = 275

# button_locations = [(310, 10), (610, 10), (910, 10), (10, 10), (10, 260),
#                     (10, 510), (910, 260), (310, 510), (610, 510), (910, 510)]
# random.shuffle(button_locations)
#
# button_list = [WhatTimeButton(button_locations[x - 1][0], button_locations[x - 1][1], pic_list[x - 1]) for x in range(10)]
# answer = ""
#
#
# def stop_sounds():
#     pygame.mixer.Sound.stop(bath_audio)
#     pygame.mixer.Sound.stop(bed_audio)
#     pygame.mixer.Sound.stop(breakfast_audio)
#     pygame.mixer.Sound.stop(dinner_audio)
#     pygame.mixer.Sound.stop(dream_audio)
#     pygame.mixer.Sound.stop(homework_audio)
#     pygame.mixer.Sound.stop(lunch_audio)
#     pygame.mixer.Sound.stop(snack_audio)
#     pygame.mixer.Sound.stop(study_audio)
#     pygame.mixer.Sound.stop(wake_up_audio)
#
#
# def refresh_question():
#     global button_list
#     global what_time_timer
#     global button_locations
#     global pic_list
#     global audio_list
#     global answer
#     stop_sounds()
#     answer = random.choice(audio_list)
#     random.shuffle(button_locations)
#     random.shuffle(pic_list)
#     button_list = [WhatTimeButton(button_locations[x - 1][0], button_locations[x - 1][1], pic_list[x - 1]) for x
#                    in range(10)]
#     game_window.blit(game_surface, (0, 0))
#     for buttons in button_list:
#         buttons.draw_button()
#     what_time_timer.draw_timer()

#
# def what_time_transition_screen():
#     # First Blip
#     game_surface.fill(BLACK)
#     game_window.blit(game_surface, (0, 0))
#     pygame.display.update()
#     pygame.time.delay(100)
#     game_surface.fill(LIGHT_GREEN)
#     game_window.blit(game_surface, (0, 0))
#     game_window.blit(transition_font.render("3", True, (0, 0, 0)), (500, 190))
#     pygame.mixer.Sound.play(countdown_sound)
#     pygame.display.update()
#     pygame.time.delay(900)
#     # Second Blip
#     game_surface.fill(BLACK)
#     game_window.blit(game_surface, (0, 0))
#     pygame.display.update()
#     pygame.time.delay(100)
#     game_surface.fill(LIGHT_GREEN)
#     game_window.blit(game_surface, (0, 0))
#     game_window.blit(transition_font.render("2", True, (0, 0, 0)), (500, 190))
#     pygame.display.update()
#     pygame.time.delay(900)
#     # Third Blip
#     game_surface.fill(BLACK)
#     game_window.blit(game_surface, (0, 0))
#     pygame.display.update()
#     pygame.time.delay(100)
#     game_surface.fill(LIGHT_GREEN)
#     game_window.blit(game_surface, (0, 0))
#     game_window.blit(transition_font.render("1", True, (0, 0, 0)), (500, 190))
#     pygame.display.update()
#     pygame.time.delay(900)
#     pygame.display.update()
#     # Go Blip
#     game_surface.fill(BLACK)
#     game_window.blit(game_surface, (0, 0))
#     pygame.display.update()
#     pygame.time.delay(100)
#     game_surface.fill(LIGHT_GREEN)
#     game_window.blit(game_surface, (0, 0))
#     game_window.blit(transition_font.render("GO", True, (0, 0, 0)), (320, 190))
#     pygame.display.update()
#     pygame.time.delay(1000)
#     pygame.display.update()
#     pygame.time.delay(150)
#
#
# # Create the menu buttons
# what_time_menu_button_1 = MenuButton(390, 230, GREEN)
# what_time_ending_button_1 = MenuButton(240, 520, RED)
# what_time_ending_button_2 = MenuButton(640, 520, GREEN)
# what_time_ending_button_1.width, what_time_ending_button_1.height = 300, 150
# what_time_ending_button_2.width, what_time_ending_button_2.height = 300, 150


# This Can Be Preserved
# def draw_menu():
#     game_window.blit(game_surface, (0, 0))
#     # Draw the buttons
#     what_time_menu_button_1.draw_button()
#     menu_title = menu_font.render("What time is it?", True, (0, 0, 0), )
#     game_window.blit(menu_title, (190, 70))
#     start_button_text = menu_font.render("START", True, (0, 0, 0), )
#     game_window.blit(start_button_text, (425, 310))
#     game_window.blit(timer_font.render(f"High Score:  {high_score}", True, (0, 0, 0),), (427, 600))
#     # game_window.blit(font.render(f"Current Score:  {score}", True, (0, 0, 0),), (812, 430))
#     pygame.display.update()
#
#
# # This Can be Preserved
# def draw_game_over_menu():
#     global high_score
#     global score
#     stop_sounds()
#     if score > high_score:
#         high_score = score
#     game_window.blit(game_surface, (0, 0))
#     what_time_ending_button_1.draw_button()
#     game_window.blit(cross, (335, 540))
#     what_time_ending_button_2.draw_button()
#     game_window.blit(check, (740, 540))
#     # game_window.blit(menu_font.render("Game Over!", True, (0, 0, 0), ), (190, 70))
#     game_window.blit(timer_font.render(f"High Score:  {high_score}", True, (0, 0, 0),), (427, 450))
#     game_window.blit(end_score_font.render(f"Final Score:  {score}", True, (0, 0, 0),), (290, 180))
#     game_window.blit(end_banner, (40, 10))
#     pygame.display.update()

#
# for buttons in button_list:
#     buttons.draw_button()
# what_time_timer.draw_timer()
# Game Loop
# game_state = "what time menu"
# running = True
# while running:
#     ev = pygame.event.get()
    # if game_state == "what time menu":
    #     draw_menu()
    #     for event in ev:
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if what_time_menu_button_1.rect.collidepoint(event.pos):
    #                 game_state = "what time load"
    # elif game_state == "what time load":
    #     what_time_transition_screen()
    #     refresh_question()
    #     pygame.event.clear()
    #     pygame.mixer.Sound.play(what_time_audio_dictionary[answer])
    #     print(answer)
    #     game_state = "what time play"
    # # elif game_state == "test":
    # #     for event in ev:
    # #         if event.type == pygame.QUIT:
    # #             running = False
    # elif game_state == "what time play":
    #     pygame.display.update()
    #     if counter == 0:
    #         game_state = "what time end"
    #     for event in ev:
    #         if event.type == pygame.USEREVENT:
    #             counter -= 1
    #             what_time_timer.draw_timer()
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             for buttons in button_list:
    #                 if buttons.rect.collidepoint(event.pos):
    #                     if buttons.name == answer:
    #                         score += 1
    #                         stop_sounds()
    #                         pygame.mixer.Sound.play(correct_sound)
    #                     else:
    #                         score -= 1
    #                         stop_sounds()
    #                         pygame.mixer.Sound.play(wrong_sound)
    #                     pygame.time.delay(300)
    #                     print(score)
    #                     refresh_question()
    #                     pygame.mixer.Sound.play(what_time_audio_dictionary[answer])
    #                     pygame.time.delay(100)
    #                     pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    #                     print(answer)
    # elif game_state == "what time end":
    #     draw_game_over_menu()
    #     for event in ev:
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if what_time_ending_button_1.rect.collidepoint(event.pos):
    #                 running = False
    #             if what_time_ending_button_2.rect.collidepoint(event.pos):
    #                 score = 0
    #                 counter = 60
    #                 game_state = "what time load"