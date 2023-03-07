import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS,SMALL_CACTUS,BIRD
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SCREEN_WIDTH


class ObstacleManager:


    def __init__(self):
        self.obstacles = []
        self.type_cactus = random.randint(0,1)
        self.bird_true = random.randint(0,40)
        self.bird = Bird()
        self.bird.bird_rect.x = 2000
        self.bird.bird_rect.y = 140
        self.bird.probability = random.randint(0,2)


    def update (self,game):
        if  self.type_cactus == 0:
            
            if len(self.obstacles) == 0:
                print(len(self.obstacles))
                cactus = Cactus(SMALL_CACTUS)
                cactus.rect.y = 325
                self.obstacles.append(cactus)

        elif self.type_cactus == 1:

            if len(self.obstacles) == 0:
                print(len(self.obstacles))
                cactus = Cactus(LARGE_CACTUS)
                cactus.rect.y = 300
                self.obstacles.append(cactus)

        if self.bird.step_index >= 10:
            self.bird.step_index = 0

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            self.type_cactus = random.randint(0,1)
            self.bird.image = BIRD[0] if self.bird.step_index <5 else BIRD[1]
            self.bird.step_index += 1
            self.bird.bird_rect.x -= self.bird.game_speed
        
            
            if game.player.dino_rect.colliderect(obstacle.rect) or game.player.dino_rect.colliderect(self.bird.bird_rect):
                game.playing = False
                break

            elif self.bird.bird_rect.x == -0:

                if self.bird.probability == 0:
                    self.bird.bird_rect.y = 100

                elif self.bird.probability == 1:
                    self.bird.bird_rect.y = 200

                elif self.bird.probability == 2:
                    self.bird.bird_rect.y = 300

                self.bird.bird_rect.x = 2000
                self.bird.probability = random.randint(0,2)


    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            self.bird.draw(screen)

