import pygame
import random

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
if screen_width == 1280:
    window_width, window_height = screen_width-180, screen_height-90
    resize_factor = 7/10
elif screen_width == 1680:
    window_width, window_height = screen_width - 110, screen_height - 60
    resize_factor = 1/2
else:
    # window_width, window_height = screen_width - 820, screen_height - 370
    # resize_factor = 7/10
    # print(window_width)
    # print(window_height)
    window_width, window_height = screen_width - 350, screen_height - 60
    resize_factor = 1
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bullet de Bulletz")
game_surface = pygame.Surface((2000, 2000))
game_surface.fill((255, 255, 255))
game_window.blit(game_surface, (0, 0))


TIME_INTERVAL = 100
pygame.time.set_timer(pygame.USEREVENT, TIME_INTERVAL)

BLACK = (255, 255, 255)
resize_factor = 1
move = 30

class Player:
    def __init__(self):
        self.x = 600
        self.y = 500
        self.size = 30
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw_player(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y , self.size, self.size))
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def increase_size(self):
        self.size += 20
        self.x -= 10
        self.y -= 10
        self.draw_player()

    def move_right(self):
        self.x = self.x + move
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_left(self):
        self.x = self.x - move
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_up(self):
        self.y = self.y - move
        game_window.blit(game_surface, (0, 0))
        self.draw_player()

    def move_down(self):
        self.y = self.y + move
        game_window.blit(game_surface, (0, 0))
        self.draw_player()


class Bullets:
    def __init__(self):
        self.length = random.randint(10, 20)
        self.rbg = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
        self.height = self.length
        self.orientation = "confused"
        self.lateral_orientation = "wtf"
        self.x = random.randint(-50, 1600)
        if self.x == 0:
            self.x = -50
            self.y = random.randint(0, 1000)
            if self.y > 500:
                self.orientation = "up"
            elif self.y < 500:
                self.orientation = "down"
            else:
                self.orientation = "straight"
            self.lateral_orientation = "right"
        elif self.x <= 100:
            self.x = -50
            self.y = random.randint(0, 1000)
            if self.y > 500:
                self.orientation = "up"
            elif self.y < 500:
                self.orientation = "down"
            else:
                self.orientation = "straight"
            self.lateral_orientation = "right"
        elif self.x == 1600:
            self.lateral_orientation = "left"
            self.y = random.randint(0, 1000)
            if self.y > 500:
                self.orientation = "up"
            elif self.y < 500:
                self.orientation = "down"
            else:
                self.orientation = "straight"
        elif self.x >= 1500:
            self.x = 1600
            self.lateral_orientation = "left"
            self.y = random.randint(0, 1000)
            if self.y > 500:
                self.orientation = "up"
            elif self.y < 500:
                self.orientation = "down"
            else:
                self.orientation = "straight"
        else:
            top_or_bottom_roll = random.randint(0, 1)
            if top_or_bottom_roll == 0:
                self.y = -50
                self.orientation = "down"
                if self.x < 800:
                    self.lateral_orientation = "right"
                elif self.x > 800:
                    self.lateral_orientation = "left"
                else:
                    self.lateral_orientation = "straight"
            if top_or_bottom_roll == 1:
                self.y = 1050
                self.orientation = "up"
                if self.x < 800:
                    self.lateral_orientation = "right"
                elif self.x > 800:
                    self.lateral_orientation = "left"
                else:
                    self.lateral_orientation = "straight"
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def render_bullet(self):
        pygame.draw.rect(game_window, self.rbg,
                         (self.x, self.y, self.height, self.length),)
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def advance_bullet(self):
        pygame.draw.rect(game_window, (255, 255, 255),
                         (self.x, self.y, self.height, self.length),)
        if self.lateral_orientation == "left":
            self.x -= 1
        elif self.lateral_orientation == "right":
            self.x += 1
        else:
            self.x = self.x
        if self.orientation == "up":
            self.y -= 1
        elif self.orientation == "down":
            self.y += 1
        else:
            self.y = self.y
        self.render_bullet()


player = Player()
player.draw_player()
bullet_list = [Bullets() for x in range(1)]
for items in bullet_list:
    items.render_bullet()
pygame.display.update()

running = True
game_state = "game"
PROBABILITY = 94

while running:
    if game_state == "game":
        for bullets in bullet_list:
            if bullets.rect.colliderect(player):
                bullets.rbg = (255, 255, 255)
                bullets.render_bullet()
                bullet_list.remove(bullets)
                player.increase_size()
                if player.size >= 1000:
                    running = False
        pygame.display.update()
        ev = pygame.event.get()
        for bullets in bullet_list:
            bullets.advance_bullet()
            if bullets.x < -100 or bullets.x > 2000:
                bullet_list.remove(bullets)
            elif bullets.y < -100 or bullets.y > 2000:
                bullet_list.remove(bullets)
        for event in ev:
            if event.type == pygame.USEREVENT:
                chance_to_spawn_bullet = random.randint(0, 100)
                if chance_to_spawn_bullet > PROBABILITY:
                    new_bullet = Bullets()
                    bullet_list.append(new_bullet)
                    PROBABILITY -= 1
                print(len(bullet_list))
                # pygame.time.set_timer(pygame.USEREVENT, TIME_INTERVAL)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()
                elif event.key == pygame.K_DOWN:
                    player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                pygame.display.update()
            if event.type == pygame.QUIT:
                running = False

