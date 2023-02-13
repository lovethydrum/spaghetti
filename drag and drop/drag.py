import pygame
import random
import os
import ctypes

# Stop Windows scaling and center the display
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
if screen_width == 1280:
    window_width, window_height = screen_width-335, screen_height - 150
    resize_factor = (6/10)
elif screen_width == 1680:
    window_width, window_height = screen_width - 110, screen_height - 60
    resize_factor = 1
else:
    window_width, window_height = screen_width - 350, screen_height - 60
    resize_factor = 1
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Direction Game")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))


BLACK = (0, 0, 0)
block_font = pygame.font.Font(None, 70)


block_coordinate_list = [[10, 10], [120, 10], [230, 10], [340, 10], [450, 10], [560, 10], [670, 10], [780, 10],
                         [890, 10], [1000, 10], [10, 120], [120, 120], [230, 120], [340, 120],
                         [450, 120], [560, 120], [670, 120], [780, 120], [890, 120], [1000, 120],
                        [10, 230], [120, 230], [230, 230], [340, 230], [450, 230], [560, 230]]
random.shuffle(block_coordinate_list)

alphabet_list = {
    "A": block_coordinate_list[0],
    "B": block_coordinate_list[1],
    "C": block_coordinate_list[2],
    "D": block_coordinate_list[3],
    "E": block_coordinate_list[4],
    "F": block_coordinate_list[5],
    "G": block_coordinate_list[6],
    "H": block_coordinate_list[7],
    "I": block_coordinate_list[8],
    "J": block_coordinate_list[9],
    "K": block_coordinate_list[10],
    "L": block_coordinate_list[11],
    "M": block_coordinate_list[12],
    "N": block_coordinate_list[13],
    "O": block_coordinate_list[14],
    "P": block_coordinate_list[15],
    "Q": block_coordinate_list[16],
    "R": block_coordinate_list[17],
    "S": block_coordinate_list[18],
    "T": block_coordinate_list[19],
    "U": block_coordinate_list[20],
    "V": block_coordinate_list[21],
    "W": block_coordinate_list[22],
    "X": block_coordinate_list[23],
    "Y": block_coordinate_list[24],
    "Z": block_coordinate_list[25],
}


class Block:
    def __init__(self, alphabet, x, y):
        self.color = (220, 50, 113)
        self.alphabet = alphabet
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        game_window.blit(block_font.render(f"{self.alphabet}", True, (0, 0, 0), ), (self.x + 34, self.y + 30))

    def draw_drag_button(self, x, y):
        pygame.draw.rect(game_window, self.color, (self.x-50, self.y-50, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x-50, self.y-50, self.width, self.height), 4)
        game_window.blit(block_font.render(f"{self.alphabet}", True, (0, 0, 0), ), (self.x - 24, self.y - 20))

    def drag_function(self):
        global blocks_list
        game_window.blit(game_surface, (0, 0))
        for things in blocks_list:
            if things.alphabet == self.alphabet:
                pass
            else:
                things.draw_button()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)
        # pygame.draw.rect(game_window, (255, 255, 255), (self.x-50, self.y-50, self.width, self.height))
        # pygame.draw.rect(game_window, (255, 255, 255), (self.x-50, self.y-50, self.width, self.height), 4)
        self.x, self.y = pygame.mouse.get_pos()
        # self.draw_drag_button(self.x, self.y)
        # pygame.display.update()


blocks_list = [Block(alphabet, alphabet_list[alphabet][0], alphabet_list[alphabet][1]) for alphabet in alphabet_list]
for items in blocks_list:
    items.draw_button()

running = True
dragging = False

while running:
    ev = pygame.event.get()
    pos = pygame.mouse.get_pos()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for blocks in blocks_list:
                if blocks.rect.collidepoint(event.pos):
                    pygame.mouse.set_pos(blocks.x + 50, blocks.y + 50)
                    # pygame.draw.rect(game_window, (255, 255, 255), (blocks.x, blocks.y, blocks.width, blocks.height))
                    # pygame.draw.rect(game_window, (255, 255, 255), (blocks.x, blocks.y, blocks.width, blocks.height), 4)
                    blocks.clicked = True
                    dragging = True
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            for blocks in blocks_list:
                blocks.clicked = False
                dragging = False
        elif dragging:
            for blocks in blocks_list:
                if blocks.clicked:
                     blocks.drag_function()
        # for items in blocks_list:
        #     items.draw_button()
    pygame.display.update()