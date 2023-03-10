from dino_runner.components.power_ups.power_up import PowerUp
from pygame.sprite import Sprite

from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):
    
    def __init__(self):
        self.image = HAMMER[0]
        super().__init__(self.image,HAMMER_TYPE)
