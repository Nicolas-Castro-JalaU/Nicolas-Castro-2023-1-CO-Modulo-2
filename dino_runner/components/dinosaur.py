import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING,RUNNING_SHIELD,RUNNING_HAMMER,JUMPING,JUMPING_SHIELD,JUMPING_HAMMER, DUCKING,DUCKING_SHIELD,DUCKING_HAMMER,DEFAULT_TYPE,SHIELD_TYPE,HAMMER_TYPE,SOUNDS


RUN_IMG = {DEFAULT_TYPE:RUNNING, SHIELD_TYPE: RUNNING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER} 
JUMP_IMG = {DEFAULT_TYPE:JUMPING,SHIELD_TYPE:JUMPING_SHIELD,HAMMER_TYPE:JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE:DUCKING,SHIELD_TYPE:DUCKING_SHIELD,HAMMER_TYPE:DUCKING_HAMMER}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5

    def __init__(self,game):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.sound = False
        self.jump_speed = self.JUMP_SPEED
        self.has_power_up= False
        self.score = 10
        self.power_time_up = 0

    def update(self,user_input,game):
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.sound = False
            if not self.sound:
                SOUNDS[0].play()
            else:
                SOUNDS[0].stop()

            if self.dino_rect.y < 290:
                self.dino_jump = False
                
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
            

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        
        if user_input[pygame.K_DOWN]:

            if self.dino_rect.y < 310:
                self.dino_duck = False
                if self.dino_rect.y < 130:
                    self.jump_speed -= 2


            elif self.dino_rect.y == 310 or self.dino_rect.y == 350:
                SOUNDS[0].stop()
                self.dino_duck = True
                self.dino_jump = False
                self.dino_run = False
                if game.game_speed < 50:
                    game.game_speed += 0.8

        if self.step_index >= 10:
            self.step_index = 0
            
 
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()
            self.sound = True

        elif self.dino_duck:
            self.duck()

    def run(self):

        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 350
        self.step_index += 1


    def jump(self):
        self.image = JUMP_IMG [self.type]
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))

    def reset(self):
        self.type = DEFAULT_TYPE
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED