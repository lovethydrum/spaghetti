import pygame
import time
import random
import ctypes
import os

# Stop Windows scaling and center the display
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Create game window
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

if screen_width == 1280:
    window_width, window_height = screen_width - 30, screen_height - 29
    resize_factor = (1250/1670)
else:
    window_width, window_height = screen_width - 250, screen_height - 50
    resize_factor = 1
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Memory Game")
cream_surface = pygame.Surface((6000, 6000))
cream_surface.fill((239, 222, 205))

game_window.blit(cream_surface, (0, 0))
player_image_raw = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image_raw, (int(125*resize_factor), int(125*resize_factor)))
font = pygame.font.Font('MitsuEHandwriting-R.otf', int(30*resize_factor))
big_font = pygame.font.Font('MitsuEHandwriting-R.otf', int(50*resize_factor))
end_font = pygame.font.Font('MitsuEHandwriting-R.otf', int(100*resize_factor))
flip_count = 0
alphabet_list = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
                 "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
                 "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Cards:
    def __init__(self, x, y):
        self.lower_color = (255, 105, 97)
        self.color = (124, 185, 232)
        self.x = x*resize_factor
        self.y = y*resize_factor
        self.letter = ""
        self.width = 100*resize_factor
        self.height = 120*resize_factor
        self.clicked_color = (211, 211, 211)
        self.highlight = (100, 100, 100)
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_card(self):
        if self.letter.islower():
            pygame.draw.rect(game_window, self.lower_color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        else:
            pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)

    def highlight_effect(self):
        if not self.clicked:
            pygame.draw.rect(game_window, self.highlight, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)

    def flip_card(self):
        pygame.draw.rect(game_window, self.clicked_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        if self.letter.isupper():
            reveal_letter = big_font.render(self.letter, True, (0, 0, 0), )
            reveal_letter_rect = reveal_letter.get_rect(center=((self.x+self.width/2), ((5+self.y)+self.height/2)))
            game_window.blit(reveal_letter, reveal_letter_rect)
        else:
            reveal_letter = big_font.render(self.letter, True, (0, 0, 0), )
            reveal_letter_rect = reveal_letter.get_rect(center=((self.x+self.width/2), (self.y+self.height/2)))
            game_window.blit(reveal_letter, reveal_letter_rect)
        global flip_count
        flip_count += 1


attempt_count = 0


def increase_attempt_count():
    return attempt_count + 1


# Y coordinates
ROW_1 = 15
ROW_2 = ROW_1 + 125
ROW_3 = ROW_2 + 125
ROW_4 = ROW_3 + 125
ROW_5 = ROW_4 + 125
ROW_6 = ROW_5 + 125
ROW_7 = ROW_6 + 125
ROW_8 = ROW_7 + 125

# X coordinates
COL_1 = 25
COL_2 = COL_1 + 200
COL_3 = COL_2 + 200
COL_4 = COL_3 + 200
COL_5 = COL_4 + 200
COL_6 = COL_5 + 200
COL_7 = COL_6 + 200
COL_8 = COL_7 + 200

# Alternate X coordinates for rows with 6
ALT_COL_1 = COL_1 + 100
ALT_COL_2 = COL_2 + 100
ALT_COL_3 = COL_3 + 100
ALT_COL_4 = COL_4 + 100
ALT_COL_5 = COL_5 + 100
ALT_COL_6 = COL_6 + 100
ALT_COL_7 = COL_7 + 100

# Card list
card_1 = Cards(COL_1, ROW_1)
card_2 = Cards(COL_2, ROW_1)
card_3 = Cards(COL_3, ROW_1)
card_4 = Cards(COL_4, ROW_1)
card_5 = Cards(COL_5, ROW_1)
card_6 = Cards(COL_6, ROW_1)
card_7 = Cards(COL_7, ROW_1)
card_8 = Cards(ALT_COL_1, ROW_2)
card_9 = Cards(ALT_COL_2, ROW_2)
card_10 = Cards(ALT_COL_3, ROW_2)
card_11 = Cards(ALT_COL_4, ROW_2)
card_12 = Cards(ALT_COL_5, ROW_2)
card_13 = Cards(ALT_COL_6, ROW_2)
card_14 = Cards(COL_1, ROW_3)
card_15 = Cards(COL_2, ROW_3)
card_16 = Cards(COL_3, ROW_3)
card_17 = Cards(COL_4, ROW_3)
card_18 = Cards(COL_5, ROW_3)
card_19 = Cards(COL_6, ROW_3)
card_20 = Cards(COL_7, ROW_3)
card_21 = Cards(ALT_COL_1, ROW_4)
card_22 = Cards(ALT_COL_2, ROW_4)
card_23 = Cards(ALT_COL_3, ROW_4)
card_24 = Cards(ALT_COL_4, ROW_4)
card_25 = Cards(ALT_COL_5, ROW_4)
card_26 = Cards(ALT_COL_6, ROW_4)
card_27 = Cards(COL_1, ROW_5)
card_28 = Cards(COL_2, ROW_5)
card_29 = Cards(COL_3, ROW_5)
card_30 = Cards(COL_4, ROW_5)
card_31 = Cards(COL_5, ROW_5)
card_32 = Cards(COL_6, ROW_5)
card_33 = Cards(COL_7, ROW_5)
card_34 = Cards(ALT_COL_1, ROW_6)
card_35 = Cards(ALT_COL_2, ROW_6)
card_36 = Cards(ALT_COL_3, ROW_6)
card_37 = Cards(ALT_COL_4, ROW_6)
card_38 = Cards(ALT_COL_5, ROW_6)
card_39 = Cards(ALT_COL_6, ROW_6)
card_40 = Cards(COL_1, ROW_7)
card_41 = Cards(COL_2, ROW_7)
card_42 = Cards(COL_3, ROW_7)
card_43 = Cards(COL_4, ROW_7)
card_44 = Cards(COL_5, ROW_7)
card_45 = Cards(COL_6, ROW_7)
card_46 = Cards(COL_7, ROW_7)
card_47 = Cards(ALT_COL_1, ROW_8)
card_48 = Cards(ALT_COL_2, ROW_8)
card_49 = Cards(ALT_COL_3, ROW_8)
card_50 = Cards(ALT_COL_4, ROW_8)
card_51 = Cards(ALT_COL_5, ROW_8)
card_52 = Cards(ALT_COL_6, ROW_8)

card_list = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12, card_13,
             card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22, card_23, card_24, card_25,
             card_26, card_27, card_28, card_29, card_30, card_31, card_32, card_33, card_34, card_35, card_36, card_37,
             card_38, card_39, card_40, card_41, card_42, card_43, card_44, card_45, card_46, card_47, card_48, card_49,
             card_50, card_51, card_52]


class Players:
    def __init__(self, name, y):
        self.score = 0
        self.name = name
        self.x = 1340*resize_factor
        self.y = y*resize_factor
        self.box_width = 300*resize_factor
        self.box_height = 180*resize_factor
        self.letter_bank = ""
        self.letter_bank_2 = ""
        self.letter_bank_3 = ""
        self.letter_bank_4 = ""
        self.letter_bank_5 = ""

    def increase_score(self):
        self.score = self.score + 1
        if self.score <= 6:
            self.letter_bank = self.letter_bank + choices[0].letter.upper() + ", "
        elif self.score <= 12:
            self.letter_bank_2 = self.letter_bank_2 + choices[0].letter.upper() + ", "
        elif self.score <= 18:
            self.letter_bank_3 = self.letter_bank_3 + choices[0].letter.upper() + ", "
        elif self.score <= 24:
            self.letter_bank_4 = self.letter_bank_4 + choices[0].letter.upper() + ", "
        else:
            self.letter_bank_5 = self.letter_bank_5 + choices[0].letter.upper() + ", "
        pygame.draw.rect(game_window, (255, 255, 255), (self.x, self.y, self.box_width, self.box_height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.box_width, self.box_height), 5)
        bank_letters = font.render(f"{self.letter_bank}", True, (0, 0, 0), )
        game_window.blit(bank_letters, (self.x + (13*resize_factor), self.y))
        bank_letters_2 = font.render(f"{self.letter_bank_2}", True, (0, 0, 0), )
        game_window.blit(bank_letters_2, (self.x + (13*resize_factor), self.y + (35*resize_factor)))
        bank_letters_3 = font.render(f"{self.letter_bank_3}", True, (0, 0, 0), )
        game_window.blit(bank_letters_3, (self.x + (13*resize_factor), self.y + (70*resize_factor)))
        bank_letters_4 = font.render(f"{self.letter_bank_4}", True, (0, 0, 0), )
        game_window.blit(bank_letters_4, (self.x + (13*resize_factor), self.y + (105*resize_factor)))
        bank_letters_5 = font.render(f"{self.letter_bank_5}", True, (0, 0, 0), )
        game_window.blit(bank_letters_5, (self.x + (13*resize_factor), self.y + (140*resize_factor)))


def generate_players(list_of_players):
    for players in list_of_players:
        player_font = font.render(f"{players.name}:  {players.score}", True, (0, 0, 0), )
        game_window.blit(player_font, (players.x, players.y - (49*resize_factor)))
        pygame.draw.rect(game_window, (255, 255, 255), (players.x, players.y, players.box_width, players.box_height))
        pygame.draw.rect(game_window, BLACK, (players.x, players.y, players.box_width, players.box_height), 5)
        bank_letters = font.render(f"{players.letter_bank}", True, (0, 0, 0), )
        game_window.blit(bank_letters, (players.x +(13*resize_factor), players.y))
        bank_letters_2 = font.render(f"{players.letter_bank_2}", True, (0, 0, 0), )
        game_window.blit(bank_letters_2, (players.x + (13*resize_factor), players.y + (35*resize_factor)))
        bank_letters_3 = font.render(f"{players.letter_bank_3}", True, (0, 0, 0), )
        game_window.blit(bank_letters_3, (players.x + (13*resize_factor), players.y + (70*resize_factor)))
        bank_letters_4 = font.render(f"{players.letter_bank_4}", True, (0, 0, 0), )
        game_window.blit(bank_letters_4, (players.x + (13*resize_factor), players.y + (105*resize_factor)))
        bank_letters_5 = font.render(f"{players.letter_bank_5}", True, (0, 0, 0), )
        game_window.blit(bank_letters_5, (players.x + (13*resize_factor), players.y + (140*resize_factor)))


# Create players
current_player = 0
player_count = 1

player_1 = Players("Player 1", 55)
player_2 = Players("Player 2", 300)
player_3 = Players("Player 3", 550)
player_4 = Players("Player 4", 800)

player_list = [player_1, player_2, player_3, player_4]


generate_players(player_list)

for entries in range(0, 52):
    card_list[entries].letter = alphabet_list[entries]

a_selection_card = Cards(90, 300)
b_selection_card = Cards(200, 300)
c_selection_card = Cards(310, 300)
d_selection_card = Cards(420, 300)
e_selection_card = Cards(530, 300)
f_selection_card = Cards(640, 300)
g_selection_card = Cards(750, 300)
h_selection_card = Cards(860, 300)
i_selection_card = Cards(970, 300)
j_selection_card = Cards(1080, 300)
k_selection_card = Cards(1190, 300)
l_selection_card = Cards(1300, 300)
m_selection_card = Cards(1410, 300)
n_selection_card = Cards(90, 500)
o_selection_card = Cards(200, 500)
p_selection_card = Cards(310, 500)
q_selection_card = Cards(420, 500)
r_selection_card = Cards(530, 500)
s_selection_card = Cards(640, 500)
t_selection_card = Cards(750, 500)
u_selection_card = Cards(860, 500)
v_selection_card = Cards(970, 500)
w_selection_card = Cards(1080, 500)
x_selection_card = Cards(1190, 500)
y_selection_card = Cards(1300, 500)
z_selection_card = Cards(1410, 500)
# selection_list = [a_selection_card, b_selection_card, c_selection_card, d_selection_card, e_selection_card,
#                   f_selection_card, g_selection_card, h_selection_card, i_selection_card, j_selection_card,
#                   k_selection_card, l_selection_card, m_selection_card, n_selection_card, o_selection_card,
#                   p_selection_card, q_selection_card, r_selection_card, s_selection_card, t_selection_card,
#                   u_selection_card, v_selection_card, w_selection_card, x_selection_card, y_selection_card,
#                   z_selection_card]


def menu_text():
    range_text = end_font.render("Choose range", True, (0, 0, 0), )
    a_text = font.render("A", True, (0, 0, 0), )
    b_text = font.render("B", True, (0, 0, 0), )
    c_text = font.render("C", True, (0, 0, 0), )
    d_text = font.render("D", True, (0, 0, 0), )
    e_text = font.render("E", True, (0, 0, 0), )
    f_text = font.render("F", True, (0, 0, 0), )
    g_text = font.render("G", True, (0, 0, 0), )
    h_text = font.render("H", True, (0, 0, 0), )
    i_text = font.render("I", True, (0, 0, 0), )
    j_text = font.render("J", True, (0, 0, 0), )
    k_text = font.render("K", True, (0, 0, 0), )
    l_text = font.render("L", True, (0, 0, 0), )
    m_text = font.render("M", True, (0, 0, 0), )
    n_text = font.render("N", True, (0, 0, 0), )
    o_text = font.render("O", True, (0, 0, 0), )
    p_text = font.render("P", True, (0, 0, 0), )
    q_text = font.render("Q", True, (0, 0, 0), )
    r_text = font.render("R", True, (0, 0, 0), )
    s_text = font.render("S", True, (0, 0, 0), )
    t_text = font.render("T", True, (0, 0, 0), )
    u_text = font.render("U", True, (0, 0, 0), )
    v_text = font.render("V", True, (0, 0, 0), )
    w_text = font.render("W", True, (0, 0, 0), )
    x_text = font.render("X", True, (0, 0, 0), )
    y_text = font.render("Y", True, (0, 0, 0), )
    z_text = font.render("Z", True, (0, 0, 0), )

    game_window.blit(range_text, (450*resize_factor, 50*resize_factor))
    if not game_state == "range: end":
        game_window.blit(a_text, (130*resize_factor, 250*resize_factor))
    if cut_range <= 2:
        game_window.blit(b_text, (240*resize_factor, 250*resize_factor))
    if cut_range <= 4:
        game_window.blit(c_text, (350*resize_factor, 250*resize_factor))
    if cut_range <= 6:
        game_window.blit(d_text, (460*resize_factor, 250*resize_factor))
    if cut_range <= 8:
        game_window.blit(e_text, (570*resize_factor, 250*resize_factor))
    if cut_range <= 10:
        game_window.blit(f_text, (680*resize_factor, 250*resize_factor))
    if cut_range <= 12:
        game_window.blit(g_text, (790*resize_factor, 250*resize_factor))
    if cut_range <= 14:
        game_window.blit(h_text, (900*resize_factor, 250*resize_factor))
    if cut_range <= 16:
        game_window.blit(i_text, (1010*resize_factor, 250*resize_factor))
    if cut_range <= 18:
        game_window.blit(j_text, (1120*resize_factor, 250*resize_factor))
    if cut_range <= 20:
        game_window.blit(k_text, (1230*resize_factor, 250*resize_factor))
    if cut_range <= 22:
        game_window.blit(l_text, (1340*resize_factor, 250*resize_factor))
    if cut_range <= 24:
        game_window.blit(m_text, (1450*resize_factor, 250*resize_factor))
    if cut_range <= 26:
        game_window.blit(n_text, (130*resize_factor, 450*resize_factor))
    if cut_range <= 28:
        game_window.blit(o_text, (240*resize_factor, 450*resize_factor))
    if cut_range <= 30:
        game_window.blit(p_text, (350*resize_factor, 450*resize_factor))
    if cut_range <= 32:
        game_window.blit(q_text, (460*resize_factor, 450*resize_factor))
    if cut_range <= 34:
        game_window.blit(r_text, (570*resize_factor, 450*resize_factor))
    if cut_range <= 36:
        game_window.blit(s_text, (680*resize_factor, 450*resize_factor))
    if cut_range <= 38:
        game_window.blit(t_text, (790*resize_factor, 450*resize_factor))
    if cut_range <= 40:
        game_window.blit(u_text, (900*resize_factor, 450*resize_factor))
    if cut_range <= 42:
        game_window.blit(v_text, (1010*resize_factor, 450*resize_factor))
    if cut_range <= 44:
        game_window.blit(w_text, (1120*resize_factor, 450*resize_factor))
    if cut_range <= 46:
        game_window.blit(x_text, (1230*resize_factor, 450*resize_factor))
    if cut_range <= 48:
        game_window.blit(y_text, (1340*resize_factor, 450*resize_factor))
    game_window.blit(z_text, (1450*resize_factor, 450*resize_factor))


pygame.display.update()
game_running = True
game_state = "range: start"
choices = []
cut_range = 0

while game_running:
    ev = pygame.event.get()
    pygame.display.update()
    if game_state == "range: start":
        cut_range = 0
        attempt_count = 0
        pygame.draw.rect(game_window, (127, 255, 127), (30*resize_factor, 30*resize_factor, 1600*resize_factor, 900*resize_factor))
        pygame.draw.rect(game_window, BLACK, (30*resize_factor, 30*resize_factor, 1600*resize_factor, 900*resize_factor), 7)

        alphabet_list = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J",
                         "j",
                         "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T",
                         "t",
                         "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

        selection_list = [a_selection_card, b_selection_card, c_selection_card, d_selection_card, e_selection_card,
                          f_selection_card, g_selection_card, h_selection_card, i_selection_card, j_selection_card,
                          k_selection_card, l_selection_card, m_selection_card, n_selection_card, o_selection_card,
                          p_selection_card, q_selection_card, r_selection_card, s_selection_card, t_selection_card,
                          u_selection_card, v_selection_card, w_selection_card, x_selection_card, y_selection_card,
                          z_selection_card]
        card_list = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12,
                     card_13,
                     card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22, card_23, card_24,
                     card_25,
                     card_26, card_27, card_28, card_29, card_30, card_31, card_32, card_33, card_34, card_35, card_36,
                     card_37,
                     card_38, card_39, card_40, card_41, card_42, card_43, card_44, card_45, card_46, card_47, card_48,
                     card_49,
                     card_50, card_51, card_52]
        for items in card_list:
            items.clicked = False
        player_1 = Players("Player 1", 55)
        player_2 = Players("Player 2", 300)
        player_3 = Players("Player 3", 550)
        player_4 = Players("Player 4", 800)
        player_list = [player_1, player_2, player_3, player_4]
        current_player = 0
        for items in selection_list:
            items.draw_card()
        menu_text()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[1:]
                    cut_range = 0
                    game_state = "range: end"
                if b_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[2:]
                    cut_range = 2
                    game_state = "range: end"
                if c_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[3:]
                    cut_range = 4
                    game_state = "range: end"
                if d_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[4:]
                    cut_range = 6
                    game_state = "range: end"
                if e_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[5:]
                    cut_range = 8
                    game_state = "range: end"
                if f_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[6:]
                    cut_range = 10
                    game_state = "range: end"
                if g_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[7:]
                    cut_range = 12
                    game_state = "range: end"
                if h_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[8:]
                    cut_range = 14
                    game_state = "range: end"
                if i_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[9:]
                    cut_range = 16
                    game_state = "range: end"
                if j_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[10:]
                    cut_range = 18
                    game_state = "range: end"
                if k_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[11:]
                    cut_range = 20
                    game_state = "range: end"
                if l_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[12:]
                    cut_range = 22
                    game_state = "range: end"
                if m_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[13:]
                    cut_range = 24
                    game_state = "range: end"
                if n_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[14:]
                    cut_range = 26
                    game_state = "range: end"
                if o_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[15:]
                    cut_range = 28
                    game_state = "range: end"
                if p_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[16:]
                    cut_range = 30
                    game_state = "range: end"
                if q_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[17:]
                    cut_range = 32
                    game_state = "range: end"
                if r_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[18:]
                    cut_range = 34
                    game_state = "range: end"
                if s_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[19:]
                    cut_range = 36
                    game_state = "range: end"
                if t_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[20:]
                    cut_range = 38
                    game_state = "range: end"
                if u_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[21:]
                    cut_range = 40
                    game_state = "range: end"
                if v_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[22:]
                    cut_range = 42
                    game_state = "range: end"
                if w_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[23:]
                    cut_range = 44
                    game_state = "range: end"
                if x_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[24:]
                    cut_range = 46
                    game_state = "range: end"
                if y_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[25:]
                    cut_range = 48
                    game_state = "range: end"
                # if z_selection_card.rect.collidepoint(event.pos):
                #     selection_list = selection_list[26:]
                #     cut_range = 52
                #     game_state = "range: end"
            elif event.type == pygame.QUIT:
                game_running = False
    elif game_state == "range: end":
        pygame.draw.rect(game_window, (127, 255, 127), (30*resize_factor, 30*resize_factor, 1600*resize_factor, 900*resize_factor))
        pygame.draw.rect(game_window, BLACK, (30*resize_factor, 30*resize_factor, 1600*resize_factor, 900*resize_factor), 7)
        for items in selection_list:
            items.draw_card()
        menu_text()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_selection_card.rect.collidepoint(event.pos):
                    if cut_range > 0:
                        pass
                    else:
                        selection_list = selection_list[1:]
                        alphabet_list = alphabet_list[:4]
                        card_list = card_list[:4]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if c_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 4:
                        pass
                    else:
                        selection_list = selection_list[2:]
                        alphabet_list = alphabet_list[cut_range:6]
                        card_list = card_list[:(6-cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if d_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 6:
                        pass
                    else:
                        selection_list = selection_list[3:]
                        alphabet_list = alphabet_list[cut_range:8]
                        card_list = card_list[:(8-cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if e_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 8:
                        pass
                    else:
                        selection_list = selection_list[4:]
                        alphabet_list = alphabet_list[cut_range:10]
                        card_list = card_list[:(10 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if f_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 10:
                        pass
                    else:
                        selection_list = selection_list[5:]
                        alphabet_list = alphabet_list[cut_range:12]
                        card_list = card_list[:(12 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if g_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 12:
                        pass
                    else:
                        selection_list = selection_list[6:]
                        alphabet_list = alphabet_list[cut_range:14]
                        card_list = card_list[:(14 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if h_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 14:
                        pass
                    else:
                        selection_list = selection_list[7:]
                        alphabet_list = alphabet_list[cut_range:16]
                        card_list = card_list[:(16 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if i_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 16:
                        pass
                    else:
                        selection_list = selection_list[8:]
                        alphabet_list = alphabet_list[cut_range:18]
                        card_list = card_list[:(18 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if j_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 18:
                        pass
                    else:
                        selection_list = selection_list[9:]
                        alphabet_list = alphabet_list[cut_range:20]
                        card_list = card_list[:(20 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if k_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 20:
                        pass
                    else:
                        selection_list = selection_list[10:]
                        alphabet_list = alphabet_list[cut_range:22]
                        card_list = card_list[:(22 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if l_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 22:
                        pass
                    else:
                        selection_list = selection_list[11:]
                        alphabet_list = alphabet_list[cut_range:24]
                        card_list = card_list[:(24 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if m_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 24:
                        pass
                    else:
                        selection_list = selection_list[12:]
                        alphabet_list = alphabet_list[cut_range:26]
                        card_list = card_list[:(26 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if n_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 26:
                        pass
                    else:
                        selection_list = selection_list[13:]
                        alphabet_list = alphabet_list[cut_range:28]
                        card_list = card_list[:(28 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if o_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 28:
                        pass
                    else:
                        selection_list = selection_list[14:]
                        alphabet_list = alphabet_list[cut_range:30]
                        card_list = card_list[:(30 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if p_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 30:
                        pass
                    else:
                        selection_list = selection_list[15:]
                        alphabet_list = alphabet_list[cut_range:32]
                        card_list = card_list[:(32 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if q_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 32:
                        pass
                    else:
                        selection_list = selection_list[16:]
                        alphabet_list = alphabet_list[cut_range:34]
                        card_list = card_list[:(34 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if r_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 34:
                        pass
                    else:
                        selection_list = selection_list[17:]
                        alphabet_list = alphabet_list[cut_range:36]
                        card_list = card_list[:(36 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if s_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 36:
                        pass
                    else:
                        selection_list = selection_list[18:]
                        alphabet_list = alphabet_list[cut_range:38]
                        card_list = card_list[:(38 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if t_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 38:
                        pass
                    else:
                        selection_list = selection_list[19:]
                        alphabet_list = alphabet_list[cut_range:40]
                        card_list = card_list[:(40 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if u_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 40:
                        pass
                    else:
                        selection_list = selection_list[20:]
                        alphabet_list = alphabet_list[cut_range:42]
                        card_list = card_list[:(42 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if v_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 42:
                        pass
                    else:
                        selection_list = selection_list[21:]
                        alphabet_list = alphabet_list[cut_range:44]
                        card_list = card_list[:(44 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if w_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 44:
                        pass
                    else:
                        selection_list = selection_list[22:]
                        alphabet_list = alphabet_list[cut_range:46]
                        card_list = card_list[:(46 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if x_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 46:
                        pass
                    else:
                        selection_list = selection_list[23:]
                        alphabet_list = alphabet_list[cut_range:48]
                        card_list = card_list[:(48 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if y_selection_card.rect.collidepoint(event.pos):
                    if cut_range >= 48:
                        pass
                    else:
                        selection_list = selection_list[24:]
                        alphabet_list = alphabet_list[cut_range:50]
                        card_list = card_list[:(50 - cut_range)]
                        random.shuffle(alphabet_list)
                        random.shuffle(card_list)
                        for entries in range(0, len(alphabet_list)):
                            card_list[entries].letter = alphabet_list[entries]
                        game_state = "selection"
                if z_selection_card.rect.collidepoint(event.pos):
                    selection_list = selection_list[25:]
                    alphabet_list = alphabet_list[cut_range:52]
                    card_list = card_list[:(52 - cut_range)]
                    random.shuffle(alphabet_list)
                    random.shuffle(card_list)
                    for entries in range(0, len(alphabet_list)):
                        card_list[entries].letter = alphabet_list[entries]
                    game_state = "selection"
            elif event.type == pygame.QUIT:
                game_running = False
    elif game_state == "selection":
        pygame.draw.rect(game_window, (127, 255, 127), (200*resize_factor, 200*resize_factor, 1300*resize_factor, 500*resize_factor))
        pygame.draw.rect(game_window, BLACK, (200*resize_factor, 200*resize_factor, 1300*resize_factor, 500*resize_factor), 7)

        single = Cards(330, 500)
        double = Cards(630, 500)
        triple = Cards(930, 500)
        quadruple = Cards(1230, 500)
        selection_list = [single, double, triple, quadruple]
        selection_text = end_font.render("How many Players?", True, (0, 0, 0), )
        one_text = font.render("ONE", True, (0, 0, 0), )
        two_text = font.render("TWO", True, (0, 0, 0), )
        three_text = font.render("THREE", True, (0, 0, 0), )
        four_text = font.render("FOUR", True, (0, 0, 0), )
        game_window.blit(player_image, (int(resize_factor*320), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*596), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*646), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*882), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*922), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*962), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*1176), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*1206), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*1236), int(resize_factor*392)))
        game_window.blit(player_image, (int(resize_factor*1266), int(resize_factor*392)))



        game_window.blit(selection_text, (340*resize_factor, 200*resize_factor))
        game_window.blit(one_text, (342*resize_factor, 620*resize_factor))
        game_window.blit(two_text, (640*resize_factor, 620*resize_factor))
        game_window.blit(three_text, (925*resize_factor, 620*resize_factor))
        game_window.blit(four_text, (1235*resize_factor, 620*resize_factor))
        for items in selection_list:
            items.draw_card()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single.rect.collidepoint(event.pos):
                    player_list.remove(player_2)
                    player_list.remove(player_3)
                    player_list.remove(player_4)
                    player_count = 1
                    game_state = "game"
                    game_window.blit(cream_surface, (0, 0))
                    generate_players(player_list)
                    for item in card_list:
                        item.draw_card()
                if double.rect.collidepoint(event.pos):
                    player_list.remove(player_3)
                    player_list.remove(player_4)
                    player_count = 2
                    game_state = "game"
                    game_window.blit(cream_surface, (0, 0))
                    generate_players(player_list)
                    for item in card_list:
                        item.draw_card()
                if triple.rect.collidepoint(event.pos):
                    player_list.remove(player_4)
                    player_count = 3
                    game_state = "game"
                    game_window.blit(cream_surface, (0, 0))
                    generate_players(player_list)
                    for item in card_list:
                        item.draw_card()
                if quadruple.rect.collidepoint(event.pos):
                    player_count = 4
                    game_state = "game"
                    game_window.blit(cream_surface, (0, 0))
                    generate_players(player_list)
                    for item in card_list:
                        item.draw_card()
            elif event.type == pygame.QUIT:
                game_running = False
# Game state end
    elif game_state == "game":
        # Current Player Display
        if len(card_list) > 0:
            if current_player == 0:
                pygame.draw.rect(game_window, RED, (1335*resize_factor, 5*resize_factor, 145*resize_factor, 48*resize_factor), 5)
            elif current_player == 1:
                pygame.draw.rect(game_window, RED, (1335*resize_factor, 250*resize_factor, 148*resize_factor, 48*resize_factor), 5)
            elif current_player == 2:
                pygame.draw.rect(game_window, RED, (1335*resize_factor, 500*resize_factor, 148*resize_factor, 48*resize_factor), 5)
            elif current_player == 3:
                pygame.draw.rect(game_window, RED, (1335*resize_factor, 750*resize_factor, 148*resize_factor, 48*resize_factor), 5)
        for event in ev:
            # Game Completion Prompt
            if len(card_list) == 0:
                game_state = "end"
            if flip_count == 2:
                time.sleep(1)
                attempt_count = increase_attempt_count()
                for item in card_list:
                    if item.clicked:
                        choices.append(item)
            # The choice is good!
                if choices[0].letter.lower() == choices[1].letter.lower():
                    player_list[current_player].increase_score()
                    card_list.remove(choices[0])
                    card_list.remove(choices[1])
            # The choice is not so good...
                elif choices[0].letter.lower() != choices[1].letter.lower():
                    current_player = current_player + 1
                    if current_player == player_count:
                        current_player = 0
                game_window.blit(cream_surface, (0, 0))
                generate_players(player_list)
                for item in card_list:
                    item.draw_card()
                    item.clicked = False
                choices = []
                flip_count = 0
            # Click a card
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in card_list:
                    if item.rect.collidepoint(event.pos):
                        if not item.clicked:
                            item.flip_card()
                            item.clicked = True
                            letter_case_check = item.letter.isupper()
                            if letter_case_check:
                                for items in card_list:
                                    if items.letter.isupper():
                                        items.highlight_effect()
                            else:
                                for items in card_list:
                                    if items.letter.islower():
                                        items.highlight_effect()
                pygame.display.update()
            elif event.type == pygame.QUIT:
                game_running = False
    elif game_state == "end":
        pygame.draw.rect(game_window, (120, 120, 100), (180*resize_factor, 200*resize_factor, 1300*resize_factor, 500*resize_factor))
        pygame.draw.rect(game_window, BLACK, (180*resize_factor, 200*resize_factor, 1300*resize_factor, 500*resize_factor), 7)
        congratulations_text = end_font.render("Congratulations!", True, (0, 0, 0), )
        reset_text = end_font.render("Reset?", True, (0, 0, 0), )
        ending_text = end_font.render(f"Total attempts:  {attempt_count}", True, (0, 0, 0), )
        yes_box = pygame.draw.rect(game_window, (255, 10, 100), (990*resize_factor, 560*resize_factor, 240*resize_factor, 120*resize_factor))
        yes_text = end_font.render("YES", True, (0, 0, 0), )
        no_text = end_font.render("NO", True, (0, 0, 0), )
        no_box = pygame.draw.rect(game_window, (255, 10, 100), (390*resize_factor, 560*resize_factor, 240*resize_factor, 120*resize_factor))
        pygame.draw.rect(game_window, BLACK, (990*resize_factor, 560*resize_factor, 240*resize_factor, 120*resize_factor), 5)
        pygame.draw.rect(game_window, BLACK, (390*resize_factor, 560*resize_factor, 240*resize_factor, 120*resize_factor), 5)

        game_window.blit(congratulations_text, (390*resize_factor, 200*resize_factor))
        game_window.blit(ending_text, (320*resize_factor, 370*resize_factor))
        game_window.blit(reset_text, (640*resize_factor, 545*resize_factor))
        game_window.blit(yes_text, (1001*resize_factor, 550*resize_factor))
        game_window.blit(no_text, (428*resize_factor, 550*resize_factor))
        for event in ev:
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if no_box.collidepoint(event.pos):
                    game_running = False
                if yes_box.collidepoint(event.pos):
                    game_state = "range: start"
        pygame.display.update()
    pygame.display.update()
