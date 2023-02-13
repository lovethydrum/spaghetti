import pygame
import random

pygame.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 350, screen_height - 60
print(window_width)
print(window_height)
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Direction Game")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))

font = pygame.font.Font("MitsuEHandwriting-R.otf", 40)

# Art import


class Monster:
    def __init__(self, hp, speed, attack, xp, size, color):
        self.hp = hp
        self.speed = speed
        self.attack = attack
        self.xp = xp
        self.size = size
        self.color = color
        self.letter = "S"
        self.x = 785
        self.y = 280
        self.center = ((self.x + self.size / 2), ((5 + self.y) + self.size / 2))

    def draw_monster(self):
        # pygame.draw.rect(game_window, self.color, (785 - (self.size / 2), 280 - (self.size / 2), self.size, self.size))
        # game_window.blit(font.render(f"{self.letter}", True, self.color), (785 - (self.size / 2), 280 - (self.size / 2), self.size, self.size))
        monster_font = pygame.font.Font("MitsuEHandwriting-R.otf", self.size)
        reveal_letter = monster_font.render(self.letter, True, self.color, )
        reveal_letter_rect = reveal_letter.get_rect(
            center=self.center)
        game_window.blit(reveal_letter, reveal_letter_rect)


monster_1 = Monster(10, random.randint(1, 5), 2, 10, 100,
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
monster_2 = Monster(1, random.randint(1, 5), 3, 10, 50,
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
monster_3 = Monster(5, random.randint(1, 5), 2, 10, 300,
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

monster_dict = {"monster 1": {
    "hp": 10,
    "speed": 4,
    "attack": 2,
    "xp": 60,
    "size": 5,
    "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
},
    "monster 2": {
        "hp": 15,
        "speed": 5,
        "attack": 1,
        "xp": 40,
        "size": 25,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 3": {
        "hp": 20,
        "speed": 2,
        "attack": 1,
        "xp": 30,
        "size": 50,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 4": {
        "hp": 60,
        "speed": 10,
        "attack": 2,
        "xp": 200,
        "size": 100,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 5": {
        "hp": 40,
        "speed": 1,
        "attack": 5,
        "xp": 200,
        "size": 150,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 6": {
        "hp": 1,
        "speed": random.randint(2, 4),
        "attack": 20,
        "xp": 300,
        "size": 200,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 7": {
        "hp": 200,
        "speed": random.randint(2, 4),
        "attack": random.randint(10, 30),
        "xp": 500,
        "size": 400,
        "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    },
    "monster 0": {
        "hp": 5,
        "speed": 2,
        "attack": 1,
        "xp": 10000,
        "size": random.randint(10, 2000),
        "color": (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
    }
}
monster_list = ["monster 0"]
# monster_list = ["monster 1", "monster 2", "monster 3"]
monster_list_2 = ["monster 4", "monster 5", "monster 6"]
monster_list_3 = ["monster 7"]
enemy = 0


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
        random_encounter()

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
        random_encounter()

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


class BattleText:
    def __init__(self):
        self.font = pygame.font.Font(None, 50)
        self.text_1 = ""
        self.text_2 = ""
        self.text_3 = "lalalalalalalala"

    def write_text(self, script, position):
        pygame.draw.rect(game_window, (0, 0, 0), (1234, 610, 300, 300), )
        pygame.draw.rect(game_window, (255, 255, 255), (1234, 610, 300, 300), 10)
        pygame.draw.rect(game_window, (0, 0, 0), (1234, 610, 300, 300), )
        pygame.draw.rect(game_window, (0, 0, 0), (30, 610, 300, 300), )
        pygame.draw.rect(game_window, (255, 255, 255), (1234, 610, 300, 300), 10)
        pygame.draw.rect(game_window, (255, 255, 255), (30, 610, 300, 300), 10)
        game_window.blit(font.render(f"ENEMY", True, (255, 255, 255)), (1282, 630))
        game_window.blit(font.render(f"HP        {enemy.hp}", True, (255, 255, 255)), (1250, 720))
        pygame.draw.rect(game_window, (255, 255, 255), (30, 610, 300, 300), 10)
        game_window.blit(font.render(f"YOU", True, (255, 255, 255)), (115, 630))
        game_window.blit(font.render(f"HP        {player.hp}", True, (255, 255, 255)), (46, 710))

        if position == 1:
            game_window.blit(self.font.render(f"{script}", True, (255, 0, 0)), (400, 600))
        elif position == 2:
            game_window.blit(self.font.render(f"{script}", True, (255, 0, 0)), (400, 700))
        elif position == 3:
            game_window.blit(self.font.render(f"{script}", True, (255, 2, 2)), (380, 750))
            pygame.display.update()


battle_script = BattleText()


def random_encounter():
    global game_state
    global monster_dict
    global enemy
    global player
    roll = random.randint(0, 10)
    if roll == 5:
        if player.x < 800 and player.y > 600:
            chosen_enemy = random.choice(monster_list_2)
            enemy = Monster(monster_dict[chosen_enemy]["hp"], monster_dict[chosen_enemy]["speed"],
                            monster_dict[chosen_enemy]["attack"], monster_dict[chosen_enemy]["xp"],
                            monster_dict[chosen_enemy]["size"], monster_dict[chosen_enemy]["color"])
            game_state = "transition"
            game_window.blit(game_surface, (0, 0))
        elif player.x > 800 and player.y > 600:
            chosen_enemy = random.choice(monster_list_3)
            enemy = Monster(monster_dict[chosen_enemy]["hp"], monster_dict[chosen_enemy]["speed"],
                            monster_dict[chosen_enemy]["attack"], monster_dict[chosen_enemy]["xp"],
                            monster_dict[chosen_enemy]["size"], monster_dict[chosen_enemy]["color"])
            game_state = "transition"
            game_window.blit(game_surface, (0, 0))
        else:
            chosen_enemy = random.choice(monster_list)
            enemy = Monster(monster_dict[chosen_enemy]["hp"], monster_dict[chosen_enemy]["speed"],
                            monster_dict[chosen_enemy]["attack"], monster_dict[chosen_enemy]["xp"],
                            monster_dict[chosen_enemy]["size"], monster_dict[chosen_enemy]["color"])
            game_state = "transition"
            game_window.blit(game_surface, (0, 0))


player = Player()
player.draw_player()


def health_check():
    global player
    global game_state
    if player.hp <= 0:
        game_state = "game over"


def healing_effect():
    for x in range(20):
        random_size = random.randint(5, 10)
        random_x = random.randint(30, 300)
        random_y = random.randint(350, 500)
        pygame.draw.rect(game_window, (120, 255, 150), (random_x, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 250, random_y, random_size, random_size))
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 950, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 1200, random_y, random_size, random_size), )
    pygame.display.update()
    pygame.time.delay(80)
    for x in range(10):
        random_size = random.randint(2, 5)
        random_x = random.randint(50, 300)
        random_y = random.randint(200, 350)
        pygame.draw.rect(game_window, (120, 255, 150), (random_x, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 250, random_y, random_size, random_size))
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 950, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 1200, random_y, random_size, random_size), )
    pygame.display.update()
    pygame.time.delay(80)
    for x in range(5):
        random_size = random.randint(1, 3)
        random_x = random.randint(50, 300)
        random_y = random.randint(50, 200)
        pygame.draw.rect(game_window, (120, 255, 150), (random_x, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 250, random_y, random_size, random_size))
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 950, random_y, random_size, random_size), )
        pygame.draw.rect(game_window, (120, 255, 150), (random_x + 1200, random_y, random_size, random_size), )
    pygame.display.update()
    pygame.time.delay(80)


def attack_effect():
    global enemy
    rolls_list = [random.randint(300, 500) for x in range(2)]
    for x in range(2):
        # pygame.draw.rect(game_window, (220, 220, 220), (1200, rolls_list[x-1], 10, 10))
        # pygame.draw.rect(game_window, (255, 0, 0), (360+42*x, rolls_list[x-1]-((rolls_list[x-1]-275)/10)*x, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20), 30, 30))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20), 30, 30))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 2, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 2, 25, 25))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 2, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 2, 25, 25))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 3, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 3, 20, 20))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 3, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 3, 20, 20))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 4, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 4, 15, 15))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 4, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 4, 15, 15))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 5, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 5, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 5, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 5, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 6, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 6, 1, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 6, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 6, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 7, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 7, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 7, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 7, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 8, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 8, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 8, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 8, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 9, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 9, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 9, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 9, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 10, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 10, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 10, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 10, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 11, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 11, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 11, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 11, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 12, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 12, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 12, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 12, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 13, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 13, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 13, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 13, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 14, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 14, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 14, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 14, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 15, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 15, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 15, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 15, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 16, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 16, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 16, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 16, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 17, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 17, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 17, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 17, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 18, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 18, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 18, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 18, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 19, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 19, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 19, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 19, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
        pygame.draw.rect(game_window, (255, 0, 0),
                         (1200 - 21 * 20, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 20, 10, 10))
        pygame.draw.rect(game_window, (255, 0, 0),
                         (360 + 21 * 20, rolls_list[x - 1] - ((rolls_list[x - 1] - 275) / 20) * 20, 10, 10))
        pygame.display.update()
        pygame.time.delay(10)
    pygame.draw.rect(game_window, (0, 0, 0), (250, 50, 1100, 470))
    pygame.display.update()
    pygame.time.delay(50)
    pygame.draw.rect(game_window, (255, 0, 0), (825 - (enemy.size / 2), 320 - (enemy.size / 2), enemy.size, enemy.size))
    pygame.display.update()
    pygame.time.delay(50)
    pygame.draw.rect(game_window, (0, 0, 0), (250, 50, 1100, 470))
    pygame.display.update()
    pygame.time.delay(50)
    enemy.draw_monster()
    #
    # pygame.time.delay(25)
    # pygame.draw.rect(game_window, (0, 0, 0), (1200, 500, 10, 10))
    # pygame.draw.rect(game_window, (220, 220, 220), (1200, 475, 10, 10))
    # pygame.display.update()
    # pygame.time.delay(25)
    # pygame.draw.rect(game_window, (220, 220, 220), (780, 275, 10, 10))


def enemy_attack_effect():
    global enemy
    enemy_shots = [(803 - enemy.size / 2, 278 - enemy.size / 2),
                   (798 - enemy.size / 2, 278 + enemy.size / 3 - enemy.size / 2),
                   (798 - enemy.size / 2, 282 + (2*enemy.size)/3 - enemy.size / 2),
                   (803 - enemy.size / 2, 282 + enemy.size - enemy.size / 2)]
    for shots in enemy_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 2, 2))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 2, 2))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in enemy_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 2, 2))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 2, 2))
    second_shots = [(753 - enemy.size / 2, 258 - enemy.size / 2),
                   (738 - enemy.size / 2, 268 + enemy.size / 3 - enemy.size / 2),
                   (738 - enemy.size / 2, 292 + (2*enemy.size)/3 - enemy.size / 2),
                   (753 - enemy.size / 2, 302 + enemy.size - enemy.size / 2)]
    for shots in second_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 4, 4))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 4, 4))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in second_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 4, 4))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 4, 4))
    third_shots = [(723 - enemy.size / 2, 238 - enemy.size / 2),
                   (698 - enemy.size / 2, 258 + enemy.size / 3 - enemy.size / 2),
                   (698 - enemy.size / 2, 302 + (2*enemy.size)/3 - enemy.size / 2),
                   (723 - enemy.size / 2, 322 + enemy.size - enemy.size / 2)]
    for shots in third_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 8, 8))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 8, 8))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in third_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 8, 8))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 8, 8))
    fourth_shots = [(653 - enemy.size / 2, 218 - enemy.size / 2),
                   (628 - enemy.size / 2, 248 + enemy.size / 3 - enemy.size / 2),
                   (628 - enemy.size / 2, 312 + (2*enemy.size)/3 - enemy.size / 2),
                   (653 - enemy.size / 2, 342 + enemy.size - enemy.size / 2)]
    for shots in fourth_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 16, 16))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 16, 16))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in fourth_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 16, 16))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 16, 16))
    fifth_shots = [(553 - enemy.size / 2, 208 - enemy.size / 2),
                    (528 - enemy.size / 2, 243 + enemy.size / 3 - enemy.size / 2),
                    (528 - enemy.size / 2, 317 + (2 * enemy.size) / 3 - enemy.size / 2),
                    (553 - enemy.size / 2, 352 + enemy.size - enemy.size / 2)]
    for shots in fifth_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 32, 32))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 32, 32))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in fifth_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 32, 32))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 32, 32))
    sixth_shots = [(443 - enemy.size / 2, 178 - enemy.size / 2),
                   (608 - enemy.size / 2, 233 + enemy.size / 3 - enemy.size / 2),
                   (608 - enemy.size / 2, 307 + (2 * enemy.size) / 3 - enemy.size / 2),
                   (272 - enemy.size / 2, 352 + enemy.size - enemy.size / 2)]
    for shots in sixth_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 64, 64))
        pygame.draw.rect(game_window, (255, 0, 255), (1570-shots[0], shots[1], 64, 64))
    pygame.display.update()
    pygame.time.delay(100)
    for shots in sixth_shots:
        pygame.draw.rect(game_window, (0, 0, 0), (shots[0], shots[1], 64, 64))
        pygame.draw.rect(game_window, (0, 0, 0), (1570-shots[0], shots[1], 64, 64))

    seventh_shots = [(333 - enemy.size / 2, 58 - enemy.size / 2),
                   (628 - enemy.size / 2, 183 + enemy.size / 3 - enemy.size / 2),
                   (628 - enemy.size / 2, 297 + (2 * enemy.size) / 3 - enemy.size / 2),
                   (222 - enemy.size / 2, 372 + enemy.size - enemy.size / 2)]
    for shots in seventh_shots:
        pygame.draw.rect(game_window, (255, 0, 255), (shots[0], shots[1], 128, 128))
        pygame.draw.rect(game_window, (255, 0, 255), (1490-shots[0], shots[1], 128, 128))
        print(1490-shots[0])
    print(enemy.size)
    pygame.display.update()
    pygame.time.delay(100)
    pygame.display.update()
    pygame.time.delay(100)
    pygame.draw.rect(game_window, (255, 0, 122), (random.randint(50, 200), random.randint(50, 360), 256, 256))
    pygame.display.update()
    pygame.time.delay(50)
    pygame.draw.rect(game_window, (255, 0, 122), (random.randint(300, 550), random.randint(50, 360), 256, 256))
    pygame.display.update()
    pygame.time.delay(50)
    pygame.draw.rect(game_window, (255, 0, 122), (random.randint(850, 1100), random.randint(50, 360), 256, 256))
    pygame.display.update()
    pygame.time.delay(50)
    pygame.draw.rect(game_window, (255, 0, 122), (random.randint(1100, 1300), random.randint(50, 360), 256, 256))
    pygame.display.update()
    pygame.time.delay(50)
    # pygame.draw.rect(game_window, (255, 0, 122), (623 - (enemy.size / 2), 138 - (enemy.size / 2),
    #                                           324 + enemy.size, 284 + enemy.size))
    # pygame.display.update()
    # pygame.time.delay(50)
    # pygame.draw.rect(game_window, (0, 0, 0), (623 - (enemy.size / 2), 138 - (enemy.size / 2),
    #                                           324 + enemy.size, 284 + enemy.size))
    pygame.display.update()
    pygame.time.delay(70)
    enemy.draw_monster()

    # for x in range(5):
    #     random_shots.append((random.randint(int(785+(enemy.size/2)), int(985+(enemy.size/2))), random.randint(150, 450)))
    # for coords in random_shots:
    #     pygame.draw.rect(game_window, (255, 0, 255), (coords[0], coords[1], 2, 2))
    # pygame.time.delay(2000)
    # pygame.display.update()
    # pygame.time.delay(500)
    # for coords in random_shots:
    #     pygame.draw.rect(game_window, (0, 0, 0), (coords[0], coords[1], 2, 2))
    # pygame.display.update()
    # pygame.time.delay(480)
    # for coords in random_shots:
    #     if coords[0] <= 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]-250, coords[1]-100, 20, 20))
    #     elif coords[0] > 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]+250, coords[1]-100, 20, 20))
    # pygame.display.update()
    # pygame.time.delay(480)
    # for coords in random_shots:
    #     if coords[0] <= 780:
    #         pygame.draw.rect(game_window, (0, 0, 0), (coords[0]-250, coords[1]-100, 20, 20))
    #     elif coords[0] > 780:
    #         pygame.draw.rect(game_window, (0, 0, 0), (coords[0]+250, coords[1]-100, 20, 20))
    # pygame.display.update()
    # pygame.time.delay(460)
    # for coords in random_shots:
    #     if coords[0] <= 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]-150, coords[1]-50, 50, 50))
    #     elif coords[0] > 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]+150, coords[1]-50, 50, 50))
    # pygame.display.update()
    # pygame.time.delay(700)
    # for coords in random_shots:
    #     if coords[0] <= 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]+50, coords[1], 100, 100))
    #     elif coords[0] > 780:
    #         pygame.draw.rect(game_window, (255, 0, 255), (coords[0]-50, coords[1], 100, 100))
    # pygame.display.update()
    # pygame.time.delay(500)


def battle_text():
    global battle_script
    pygame.draw.rect(game_window, (255, 255, 255), (350, 560, 865, 400), 10)
    battle_script.write_text(battle_script.text_1)
    battle_script.write_text(battle_script.text_2)
    battle_script.write_text(battle_script.text_3)


def battle_display():
    global player
    global enemy
    game_surface.fill((0, 0, 0))
    game_window.blit(game_surface, (0, 0))
    pygame.draw.rect(game_window, (120, 255, 150), (30, 30, 1510, 500), 10)
    pygame.draw.rect(game_window, (120, 255, 150), (26, 26, 12, 10), )
    pygame.draw.rect(game_window, (120, 255, 150), (1533, 26, 12, 10), )
    pygame.draw.rect(game_window, (120, 255, 150), (26, 525, 12, 10), )
    pygame.draw.rect(game_window, (120, 255, 150), (1533, 525, 12, 10), )
    enemy.draw_monster()
    pygame.draw.rect(game_window, (255, 255, 255), (30, 610, 300, 300), 10)
    game_window.blit(font.render(f"HP        {player.hp}", True, (255, 255, 255)), (46, 710))
    game_window.blit(font.render(f"YOU", True, (255, 255, 255)), (115, 630))
    pygame.draw.rect(game_window, (255, 255, 255), (1234, 610, 300, 300), 10)
    game_window.blit(font.render(f"HP        {enemy.hp}", True, (255, 255, 255)), (1250, 720))
    game_window.blit(font.render(f"ENEMY", True, (255, 255, 255)), (1282, 630))
    # battle_text()
    pygame.draw.rect(game_window, (255, 255, 255), (350, 560, 865, 400), 10)
    pygame.display.update()


def transition_screen():
    game_surface.fill((0, 0, 0))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((255, 255, 255))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((0, 0, 0))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((255, 255, 255))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((0, 0, 0))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((255, 255, 255))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((0, 0, 0))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)
    game_surface.fill((255, 255, 255))
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(150)


running = True
game_state = "map"

while running:
    ev = pygame.event.get()
    pygame.display.update()
    if game_state == "map":
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()
                elif event.key == pygame.K_DOWN:
                    player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                    random_encounter()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                    random_encounter()
    if game_state == "transition":
        transition_screen()
        pygame.event.clear()
        battle_display()
        game_state = "battle"
    if game_state == "battle":
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    battle_display()
                    if enemy.speed > player.speed:
                        player.hp -= enemy.attack
                        battle_script.write_text(f"The enemy strikes first!  You take {enemy.attack} damage.", 1)
                        health_check()
                        pygame.display.update()
                        pygame.time.delay(200)
                        heal_amount = random.randint(1, 30)
                        if player.hp + heal_amount > player.max_hp:
                            heal_amount = player.max_hp - player.hp
                        player.hp += heal_amount
                        healing_effect()
                        battle_script.write_text(f"You cast heal for {heal_amount} HP.", 2)
                        pygame.display.update()
                        pygame.time.delay(200)
                    elif player.speed > enemy.speed:
                        heal_amount = random.randint(1, 30)
                        if player.hp + heal_amount > player.max_hp:
                            heal_amount = player.max_hp - player.hp
                        player.hp += heal_amount
                        healing_effect()
                        battle_script.write_text(f"You cast heal for {heal_amount} HP.", 1)
                        pygame.display.update()
                        pygame.time.delay(200)
                        battle_script.write_text(f"The enemy strikes!  You take {enemy.attack} damage.", 2)
                        player.hp -= enemy.attack
                        health_check()
                        pygame.display.update()
                        pygame.time.delay(200)
                    else:
                        roll = random.randint(0, 1)
                        if roll == 0:
                            battle_script.write_text(f"The enemy strikes first!  You take {enemy.attack} damage.", 1)
                            player.hp -= enemy.attack
                            health_check()
                            pygame.display.update()
                            pygame.time.delay(200)
                            heal_amount = random.randint(1, 30)
                            if player.hp + heal_amount > player.max_hp:
                                heal_amount = player.max_hp - player.hp
                            player.hp += heal_amount
                            healing_effect()
                            battle_script.write_text(f"You cast heal for {heal_amount} HP.", 2)
                            pygame.display.update()
                            pygame.time.delay(200)
                        if roll == 1:
                            heal_amount = random.randint(1, 30)
                            if player.hp + heal_amount > player.max_hp:
                                heal_amount = player.max_hp - player.hp
                            player.hp += heal_amount
                            healing_effect()
                            battle_script.write_text(f"You cast heal for {heal_amount} HP.", 1)
                            pygame.display.update()
                            pygame.time.delay(200)
                            battle_script.write_text(f"The enemy strikes!  You take {enemy.attack} damage.", 2)
                            player.hp -= enemy.attack
                            health_check()
                            pygame.display.update()
                            pygame.time.delay(200)
                elif event.key == pygame.K_a:
                    battle_display()
                    if enemy.speed > player.speed:
                        battle_script.write_text(f"The enemy strikes first!  You take {enemy.attack} damage.", 1)
                        player.hp -= enemy.attack
                        health_check()
                        enemy.hp = enemy.hp - player.attack
                        battle_script.write_text(f"You strike back!  The enemy takes {player.attack} damage.", 2)
                        attack_effect()
                    elif player.speed > enemy.speed:
                        attack_effect()
                        battle_script.write_text(f"You strike first!  The enemy takes {player.attack} damage.", 1)
                        pygame.display.update()
                        pygame.time.delay(500)
                        enemy.hp = enemy.hp - player.attack
                        if enemy.hp <= 0:
                            pass
                        else:
                            enemy_attack_effect()
                            battle_script.write_text(f"The enemy counters!  You take {enemy.attack} damage.", 2)
                            player.hp -= enemy.attack
                            health_check()
                    elif player.speed == enemy.speed:
                        print("EVEN MATCH!!!!!")
                        coin_flip = random.randint(0, 1)
                        if coin_flip == 0:
                            battle_script.write_text(f"The enemy strikes first!  You take {enemy.attack} damage.", 1)
                            player.hp -= enemy.attack
                            health_check()
                            enemy.hp = enemy.hp - player.attack
                            battle_script.write_text(f"You strike back!  The enemy takes {player.attack} damage.", 2)
                        if coin_flip == 1:
                            battle_script.write_text(f"You strike first!  The enemy takes {player.attack} damage.", 1)
                            enemy.hp = enemy.hp - player.attack
                            if enemy.hp <= 0:
                                pass
                            else:
                                battle_script.write_text(f"The enemy counters!  You take {enemy.attack} damage.", 2)
                                player.hp -= enemy.attack
                                health_check()
                    if enemy.hp <= 0:
                        player.xp += enemy.xp
                        player.level_check()
                        game_surface.fill((255, 255, 255))
                        game_window.blit(game_surface, (0, 0))
                        player.draw_player()
                        game_state = "map"
    if game_state == "game over":
        running = False

# Level 1 - basic sound alphabet - enemy visible
# Level 2 - combo sounds "th" - enemy visible
# Level 3 - Shapeshifters for level 1-2
# Level 4 - A dark shroud appears...
# Boss Fight
# Level 5 - 3 Letter Words - visible
# Level 6 - 5 Letter Words - visible
# Level 7 - Shapeshifters for words
# Level 8 - A darkness appears
# Boss Fight
# Final Boss Fight