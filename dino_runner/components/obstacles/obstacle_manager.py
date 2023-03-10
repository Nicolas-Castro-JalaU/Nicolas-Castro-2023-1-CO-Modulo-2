import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE


class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    self.enemy = 0

  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      self.obstacle = Cactus(cactus_type)
      self.enemy = 0
      
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      self.obstacle = Cactus(cactus_type)
      self.enemy = 0
    else:
      self.obstacle = Bird()
      self.enemy = 1
    return self.obstacle

  def update(self, game):
    if len(self.obstacles) == 0:
      obstacle_type = random.randint(0, 2)
      self.obstacle = self.generate_obstacle(obstacle_type)
      self.obstacles.append(self.obstacle)

    for self.obstacle in self.obstacles:
      self.obstacle.update(game.game_speed, self.obstacles)

      if game.player.dino_rect.colliderect(self.obstacle.rect):

        if game.player.type == SHIELD_TYPE:
            if self.enemy == 1:
              game.playing = True
            else:
              game.playing = False
              break
        elif game.player.type == HAMMER_TYPE:
          self.obstacles.remove(self.obstacle)

        else:
          game.playing = False
          break

  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)

    
  def reset_obstacles(self):
    self.obstacles = []

