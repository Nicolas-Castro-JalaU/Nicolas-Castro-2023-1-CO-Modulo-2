import pygame

from dino_runner.utils.constants import FONT_STYLE


class Counter:
  POSITION_COUNT_X = 1000
  POSITION_COUNT_Y = 50

  def __init__(self):
    self.count = 0
    
  def update(self,game):
    self.count += 1


  def draw(self,screen,message, x = POSITION_COUNT_X, y = POSITION_COUNT_Y):

    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"{message}:{self.count}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x,y)
    screen.blit(text, text_rect)

  def reset(self):
    self.count = 0
    
  def set_count(self, value):
    self.count = value

    