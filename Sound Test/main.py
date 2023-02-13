import pygame
import pygame.event
import time
import random

pygame.init()
pygame.mixer.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 50, screen_height - 50
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Memory Game")
cream_surface = pygame.Surface((6000, 6000))
cream_surface.fill((239, 222, 205))
game_window.blit(cream_surface, (0, 0))

d = pygame.image.load("bison.png")
IMAGE_SIZE = (100, 100)
e = pygame.transform.scale(d, IMAGE_SIZE)


running = True
BLACK = (0, 0, 0)

hadouken = pygame.mixer.Sound("hadouken.ogg")
womp = pygame.mixer.Sound("womp-womp.ogg")
ding = pygame.mixer.Sound("ding.ogg")
ten = pygame.mixer.Sound("ten.ogg")
apple = pygame.mixer.Sound("apple.ogg")

card_font = pygame.font.Font('MitsuEHandwriting-R.otf', 70)
next_question_font = pygame.font.Font('MitsuEHandwriting-R.otf', 100)


class Cards:
    def __init__(self, letter, x, y):
        self.color = (124, 185, 232)
        self.x = x
        self.y = y
        self.letter = letter
        self.width = 200
        self.height = 200
        self.lower_color = (100, 100, 100)
        self.clicked_color = (211, 211, 211)
        self.highlight = (100, 100, 100)
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_card(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        poo = card_font.render(f"{self.letter}", True, (0, 0, 0), )
        game_window.blit(poo, (self.x+75, self.y+50))


class Questions:
    def __init__(self, letter, sound):
        self.color = (124, 185, 232)
        self.x = 400
        self.y = 100
        self.letter = letter
        self.sound = sound
        self.lower_color = (100, 100, 100)
        self.width = 700
        self.height = 250
        self.clicked_color = (211, 211, 211)
        self.highlight = (100, 100, 100)
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_card(self):
        # if self.letter.islower():
        #     pygame.draw.rect(game_window, self.lower_color, (self.x, self.y, self.width, self.height))
        #     pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        # else:
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)

score = 0


def increase_score():
    global score
    score += 1

score_font = pygame.font.Font('MitsuEHandwriting-R.otf', 50)
score_text = score_font.render(f"Score:     {score}", True, (0, 0, 0), )
game_window.blit(score_text, (1100, 720))
S = Cards("S", 13, 500)
A = Cards("A", 263, 500)
T = Cards("T", 523, 500)
P = Cards("P", 773, 500)
I = Cards("I", 1023, 500)
N = Cards("N", 1273, 500)
H = Cards("H", 13, 500)
A = Cards("A", 263, 500)
X = Cards("X", 523, 500)
O = Cards("O", 773, 500)
R = Cards("R", 1023, 500)
Z = Cards("Z", 1273, 500)

setlist = []
not_answer = Cards("W", 1000, 400)
set_1_question_1 = Questions("S", hadouken)
set_1_question_2 = Questions("T", ten)
set_1_question_3 = Questions("A", apple)
answer_list = [set_1_question_1, set_1_question_2, set_1_question_3]
random.shuffle(answer_list)
current_question = 0
game_mode = "selection"
while running:
    ev = pygame.event.get()
    pygame.display.update()
    if game_mode == "selection":
        pygame.draw.rect(game_window, (127, 255, 127), (200, 200, 1300, 500))
        pygame.draw.rect(game_window, BLACK, (200, 200, 1300, 500), 7)

        single = Cards("A", 330, 500)
        double = Cards("B", 630, 500)
        triple = Cards("C", 930, 500)
        quadruple = Cards("D", 1230, 500)
        selection_list = [single, double, triple, quadruple]
        for items in selection_list:
            items.draw_card()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single.rect.collidepoint(event.pos):
                    setlist = [S, A, T, P, I, N]
                    game_mode = "play"
                if double.rect.collidepoint(event.pos):
                    setlist = [H, A, X, O, R, Z]
                    game_mode = "play"
                if triple.rect.collidepoint(event.pos):
                    setlist = [S, A, T, O, R, Z]
                    game_mode = "play"
                if quadruple.rect.collidepoint(event.pos):
                    setlist = [H, A, X, P, I, N]
                    game_mode = "play"
            elif event.type == pygame.QUIT:
                game_running = False
        # setlist = [H, A, X, O, R, Z]
    if game_mode == "play":
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            for items in setlist:
                items.draw_card()
            answer_list[current_question].draw_card()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answer_list[current_question].rect.collidepoint(event.pos):
                    pygame.mixer.Sound.play(answer_list[current_question].sound)
                for choices in setlist:
                    if choices.rect.collidepoint(event.pos):
                        if answer_list[current_question].letter == choices.letter:
                            pygame.mixer.Sound.play(ding)
                            increase_score()
                            game_window.blit(cream_surface, (0, 0))
                            score_font = pygame.font.Font('MitsuEHandwriting-R.otf', 50)
                            score_text = score_font.render(f"Score:     {score}", True, (0, 0, 0), )
                            game_window.blit(score_text, (1100, 720))
                            current_question = current_question + 1
                            for x in range(0, score):
                                game_window.blit(e, (random.randint(0, 1390), random.randint(0, 620)), (0, 0, 50, 50))
                            next_question_text = next_question_font.render(f"Next Question!", True, (0, 0, 0), )
                            game_window.blit(next_question_text, (350, 300))
                            pygame.display.update()
                            if current_question > len(answer_list)-1:
                                current_question = 0
                            time.sleep(2)
                            game_window.blit(cream_surface, (0, 0))
                            game_window.blit(score_text, (1100, 720))
                            pygame.mixer.Sound.play(answer_list[current_question].sound)

                        elif not answer_list[current_question].letter == choices.letter:
                            pygame.mixer.Sound.play(womp)
                            game_window.blit(cream_surface, (0, 0))
                            game_window.blit(score_text, (1100, 720))
                            current_question = current_question + 1
                            for x in range(0, score):
                                game_window.blit(e, (random.randint(0, 1390), random.randint(0, 620)))
                            next_question_text = next_question_font.render(f"Next Question!", True, (0, 0, 0), )
                            game_window.blit(next_question_text, (350, 300))
                            pygame.display.update()
                            if current_question > len(answer_list) - 1:
                                current_question = 0
                            time.sleep(2)
                            game_window.blit(cream_surface, (0, 0))
                            game_window.blit(score_text, (1100, 720))
                            pygame.mixer.Sound.play(answer_list[current_question].sound)
