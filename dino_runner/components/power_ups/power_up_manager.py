import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)
        self.duration = random.randint(3,5)
        self.ran_power_up_type = random.randint(0,1)

    def power_up_type(self):
        self.ran_power_up_type = random.randint(0,1)
        print(self.ran_power_up_type)
        if self.ran_power_up_type== 0: 
            self.power_up = Shield()

        else:
            self.power_up = Hammer()

    def generate_power_up(self):
        self.when_appears += random.randint(200,300)
        self.power_up_type()
        self.power_ups.append(self.power_up)

    def update(self,game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()

        for self.power_up in self.power_ups:
            self.power_up.update(game.game_speed,self.power_ups)

            if game.player.dino_rect.colliderect(self.power_up.rect) and self.power_up:
                self.power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = self.power_up.type
                game.player.power_time_up = self.power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(self.power_up)


    def draw(self,screen):
        for self.power_up in self.power_ups:
            self.power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)