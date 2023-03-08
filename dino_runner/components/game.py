import pygame
import random


from pygame import mixer  
from dino_runner.utils.constants import BG, CLOUD, DINO_3D,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu 



class Game:

    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 2000
        self.y_pos_cloud = [140,220,250,110,240,290]
        self.alt = 0
        self.alt2 = 4
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu("press any key to start...",self.screen)
        self.running = False
        self.score = 0
        self.death_count = 0



    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width1 = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud[self.alt]))
        self.screen.blit(CLOUD, (image_width1 + self.x_pos_cloud + 600, self.y_pos_cloud[self.alt2]))
        
        if self.x_pos_cloud <= -800:
            self.alt = random.randint(0,5)
            self.alt2 = random.randint(0,5)
            self.x_pos_cloud = 2000
            
        self.x_pos_cloud -= self.game_speed - 10
        

    def show_menu(self):

        self.menu.reset_screen_color(self.screen)
        half_screen_height = 0
        half_screen_width = 300

        if self.death_count == 0:
            self.menu.draw(self.screen)

        else:
            self.menu.update_message("new message")
            self.menu.draw(self.screen)

        
        self.screen.blit(DINO_3D[0],(half_screen_width, half_screen_height))

        self.menu.update(self)

    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 1


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"SCORE:{self.score}",True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        self.screen.blit(text,text_rect)