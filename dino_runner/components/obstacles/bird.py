import random
from random import randint
from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
       

    def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = SCREEN_WIDTH
        self.game_speed = 20
        self.bird_rect.y = 320
        self.step_index = 0
        self.probability = 0

        self.dino_fly = True
        self.bird = random.randint(28,49)

    def clear(self):

        if self.rect.x <- self.rect.width:
            self.pop()

    def update(self):

        if self.dino_fly:
            self.fly()

        if self.step_index >= 10:
            self.step_index = 0

    def fly(self):

        self.image = BIRD[0] if self.step_index <5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = SCREEN_WIDTH

        if self.probability == 0:
            self.bird_rect.y = 100

        elif self.probability == 1:
            self.bird_rect.y = 200

        elif self.probability == 2:
            self.bird_rect.y = 300

        self.bird_rect.x -= self.game_speed
        self.step_index += 1

    def draw(self,screen):

        if self.bird > 25:
            screen.blit(self.image,(self.bird_rect.x,self.bird_rect.y))
