import pygame
import random

# Create width and height constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Initialise all the pygame modules
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game windows
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
darkness_window = pygame.Surface((600, 490))
white_window = pygame.Surface((1100, 800))
white_window.fill(WHITE)
font1 = pygame.font.Font('MitsuEHandwriting-R.otf', 500)


clock = pygame.time.Clock()
counter, text = 60, "60".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 10)
clock_text = str(counter).rjust(3)

jump = pygame.USEREVENT + 1


# Class

class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 50
        self.xp = 0
        self.max_hp = 20
        self.hp = 20
        self.attack = random.randint(2, 4)
        self.level = 1
        self.level_up = [50, 150, 250, 350, 400, 600, 1000, 1500, 2000, 3000, 5000, 10000, 10000000000]
        # self.speed = random.randint(2, 4)
        self.speed = 100
        self.color = (0, 255, 255)

    def draw_player(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.size, self.size))

    def move_right(self):
        for moves in range(50):
            pygame.draw.rect(game_window, (255, 255, 255), (self.x, self.y, self.size, self.size))
            self.x = self.x + 1
            self.draw_player()
            pygame.display.update()
            pygame.time.delay(1)

    def move_left(self):
        for moves in range(50):
            pygame.draw.rect(game_window, (255, 255, 255), (self.x, self.y, self.size, self.size))
            self.x = self.x - 1
            self.draw_player()
            pygame.display.update()
            pygame.time.delay(1)

    def move_up(self):
        for moves in range(50):
            pygame.draw.rect(game_window, (255, 255, 255), (self.x, self.y, self.size, self.size))
            self.y = self.y - 1
            if self.y < 10:
                self.y = self.y + 50
                break
            else:
                self.draw_player()
                pygame.display.update()
                pygame.time.delay(1)

    def move_down(self):
        for moves in range(50):
            pygame.draw.rect(game_window, (255, 255, 255), (self.x, self.y, self.size, self.size))
            self.y = self.y + 1
            if self.y > 1000:
                self.y = self.y - 50
                break
            else:
                self.draw_player()
                pygame.display.update()
                pygame.time.delay(1)

    def level_check(self):
        if self.xp > self.level_up[self.level - 1]:
            print("LEVEL UP")
            self.xp = self.xp - self.level_up[self.level - 1]
            self.level = self.level + 1
            self.max_hp = self.max_hp + random.randint(8, 20)
            self.hp = self.max_hp
            self.attack = self.attack + random.randint(1, 3)
            roll = random.randint(0, 3)
            if roll == 1:
                self.speed = self.speed + 1
        else:
            print(f"XP: {self.xp}")


def gravity(position) -> int:
    if jumping:
        return position - 10
    else:
        return position + 5


def move_left_and_right(position) -> int:
    if walking:
        if position < 0:
            return position - 10
        elif position >0:
            return position + 10
    else:
        pass


running = True
walking = False
jumping = False
game_window.blit(white_window, (0, 0))

player = Player()

while running:
    game_window.blit(white_window, (0, 0))
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.USEREVENT:
            if not jumping:
                if player.y < 500:
                    player.y = gravity(player.y)
            else:
                player.y = gravity(player.y)
        elif event.type == pygame.USEREVENT+1:
            jumping = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not jumping and player.y >= 500:
                    jumping = True
                    pygame.time.set_timer(pygame.USEREVENT+1, 100)
            if event.key == pygame.K_RIGHT:
                walking = True
                player.x = move_left_and_right(player.x)
            if event.key == pygame.K_LEFT:
                walking = True
                player.x = move_left_and_right(-1*player.x)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                walking = False
            if event.key == pygame.K_LEFT:
                walking = False

        if event.type == pygame.QUIT:
            running = False
    player.draw_player()
    pygame.display.update()