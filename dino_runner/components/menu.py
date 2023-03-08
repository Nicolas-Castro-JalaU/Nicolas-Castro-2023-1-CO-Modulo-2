import pygame
from dino_runner.utils.constants import FONT_STYLE,SCREEN_HEIGHT,SCREEN_WIDTH

class Menu:

    half_screen_height = 530
    half_screen_width = 480

    def __init__(self,message, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width)

    def print_score(self,message):

        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width-10)

    def print_best_score(self,message):

        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width+20)

    def print_death_count(self,message):

        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width+50)

    def print_new_record(self,message):

        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width-80)

    def update(self,game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self,screen,game):

        screen.blit(self.text,self.text_rect)
            

    def reset_screen_color(self,screen):
        screen.fill((255,255,255))

    def handle_events_on_menu(self,game):

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game.running = False 
                game.playing = False
                break
            elif event.type == pygame.KEYDOWN:
                game.run()

    
         