import random
from random import randint

from dino_runner.components.obstacle import Obstacle


class Cactus(Obstacle):
    
    def __init__(self,image):
        self.image = random.randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 325