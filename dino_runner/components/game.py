import pygame
import random


from pygame import mixer  
from dino_runner.utils.constants import HEART,DEFAULT_TYPE,BG, CLOUD,SOUNDS,DINO_3D,ICON, SHIELD, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu 
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManager



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
        self.time_to_show = 0
        self.player = Dinosaur(Game)
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score_count = self.COUNT_SCORE
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        SOUNDS[3].play()
        self.music = False
        self.running = True
        while self.running:
            if not self.playing:
                SOUNDS[3].set_volume(0.0)
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.death_count.update(self)
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            actual_volume = SOUNDS[3].get_volume()
            if SOUNDS[3].get_volume() >= actual_volume:
                SOUNDS[3].set_volume(0.0)
            self.events()
            self.update()
            self.draw()
        self.time_to_show = 0
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update(self)
        self.update_score()    

    def night(self):
        if self.score_count > 200:
            self.screen.fill((0, 0, 0))

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.screen.blit(HEART,(100,20))
        self.screen.blit(HEART,(60,20))
        self.screen.blit(HEART,(20,20))


        self.draw_power_up_time()
        self.score.draw(self.screen,"SCORE")
        self.highest_score.draw(self.screen,"BEST",880)
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
        self.time_to_show = 0
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.aprox = 0
        
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'PRESS ANY KEY TO START.',half_screen_width,460)
            self.screen.blit(DINO_3D[0],(400,40))
        else:
            self.menu.draw(self.screen, 'GAME OVER',half_screen_width,20)
            self.menu.draw(self.screen, f'YOUR SCORE: {self.score.count}', half_screen_width, 420 )
            self.menu.draw(self.screen, f'BEST SCORE: {self.highest_score.count}', half_screen_width, 460 )
            self.menu.draw(self.screen, f'DEATHS: {self.death_count.count}', half_screen_width, 500 )

            if self.score.count > self.highest_score.count:
               self.aprox = self.score.count - self.highest_score.count

            else:

                self.aprox = self.highest_score.count - self.score.count

            if self.score.count >= self.highest_score.count:
                self.screen.blit(DINO_3D[3],(400,40))
                self.menu.draw(self.screen, f'NEW RECORD', half_screen_width, 360 )

            elif self.score.count > 0 and self.score.count < 500:
                if self.aprox < 100:
                    self.screen.blit(DINO_3D[4],(400,40))
                    self.menu.draw(self.screen, f'SO CLOSE', half_screen_width, 360)

                else:
                    self.screen.blit(DINO_3D[1],(400,40))
                    self.menu.draw(self.screen, f'SO BAD', half_screen_width, 360)


            elif self.score.count > 500 and self.score.count < 1000:
                if self.aprox < 100:
                    self.screen.blit(DINO_3D[4],(400,40))
                    self.menu.draw(self.screen, f'SO CLOSE', half_screen_width, 360)
                else:
                    self.screen.blit(DINO_3D[2],(400,40))
                    self.menu.draw(self.screen, f'SO BAD', half_screen_width, 360)


        self.menu.update(self)
        self.update_highest_score()
            
    def update_score(self):
        if self.score.count % 100 == 0 and self.game_speed < 100:
            self.game_speed += 0.8
        
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.time_to_show = 0 
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()

    def draw_power_up_time(self):

        if self.player.has_power_up:
            self.time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000 , 2 )

            if self.time_to_show > 0 and self.running:
                self.menu.draw(self.screen,f"{self.player.type.capitalize()} ENABLE FOR {self.time_to_show} SECONDS",500,50)
        
            else:
                self.time_to_show = 0
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE