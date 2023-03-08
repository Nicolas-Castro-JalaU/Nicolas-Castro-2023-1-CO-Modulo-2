import pygame
import random


from pygame import mixer  
from dino_runner.utils.constants import BG, CLOUD,SOUNDS,DINO_3D,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu 



class Game:

    GAME_SPEED = 20
    COUNT_SCORE = 500

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.music = True
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
        self.best_score = 0
        self.death_count = 0
        self.score_count = self.COUNT_SCORE

    def add_counter(self):
        
        if self.music:
            SOUNDS[3].play(-1)

        if self.score == self.score_count:
            self.score_count = self.score_count + self.COUNT_SCORE
            SOUNDS[1].play()
   
        if not self.playing and self.score > self.best_score:
            self.death_count =+ 1
            self.best_score = self.score

    def execute(self):
        self.add_counter()
        self.music = False
        self.running = True
        while self.running:
            if not self.playing:
                SOUNDS[3].set_volume(1.0)
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def reset_counters(self):

        self.obstacle_manager.reset_obstacles()
        #self.player.reset_dino()
        self.game_speed = self.GAME_SPEED
        self.score = 0

    def run(self):
        # Game loop: events - update - draw
        SOUNDS[3].set_volume(1.0)
        self.add_counter()
        self.reset_counters()
        self.playing = True
        while self.playing:
            actual_volume = SOUNDS[3].get_volume()
            if SOUNDS[3].get_volume() >= actual_volume:
                SOUNDS[3].set_volume(0.4)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.add_counter()
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
        self.draw_best_score()
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
        half_screen_height = -20
        half_screen_width = 350
        self.aprox = 0

        if self.death_count == 0:
            self.menu.draw(self.screen,self)
            self.screen.blit(DINO_3D[0],(half_screen_width, half_screen_height))

        elif self.death_count > 0:
                
            self.menu.print_score(f"YOUR SCORE:{self.score}")
            self.menu.draw(self.screen,self)
            self.menu.print_death_count(f"DEATH:{self.death_count}")
            self.menu.draw(self.screen,self)

            if self.score > self.best_score:
                self.aprox = self.score - self.best_score
            else:
                self.aprox = self.best_score - self.score 

            if self.score > self.best_score:
                self.menu.print_new_record("NEW RECORD!")
                self.menu.draw(self.screen,self)
                self.menu.print_best_score(f"LAST BEST SCORE:{self.best_score}")
                self.menu.draw(self.screen,self)
                self.screen.blit(DINO_3D[3],(half_screen_width, half_screen_height))

            elif self.score > 0 and self.score < 500:  
                self.menu.print_best_score(f"BEST SCORE:{self.best_score}")
                self.menu.draw(self.screen,self)
                self.screen.blit(DINO_3D[1],(half_screen_width, half_screen_height))

            elif self.score > 500 and self.score < 1000:
                self.menu.print_best_score(f"BEST SCORE:{self.best_score}")
                self.menu.draw(self.screen,self)
                self.screen.blit(DINO_3D[2],(half_screen_width, half_screen_height))

            elif self.aprox < 100:
                self.menu.print_new_record("SO CLOSE..")
                self.menu.draw(self.screen,self)
                self.menu.print_best_score(f"BEST SCORE:{self.best_score}")
                self.menu.draw(self.screen,self)
                self.screen.blit(DINO_3D[4],(half_screen_width, half_screen_height))

        self.menu.update(self)


    
    def update_score(self):
        self.score += 1
        if self.score % 1000 == 0 and self.game_speed < 500:
            self.game_speed += 1


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 20)
        text = font.render(f"SCORE:{self.score}",True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        self.screen.blit(text,text_rect)

    def draw_best_score(self):
        font = pygame.font.Font(FONT_STYLE, 20)
        text = font.render(f"BEST:{self.best_score}",True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (880,50)
        self.screen.blit(text,text_rect)