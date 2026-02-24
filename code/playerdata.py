##########player data###########3
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        ## player sprite ##
        self.image = pygame.Surface((64,64))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = pos)
        self.radius = 30
        
        ## movement ##
        self.direction = pygame.math.Vector2()
        self.walkspeed = 5
        self.sprintspeed = 10
        self.movespeed = 0
        
        self.obstacle_sprites = obstacle_sprites
        ## equipment ##
        
        
    def inputs(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT]:
            self.movespeed = self.sprintspeed
        else:
            self.movespeed = self.walkspeed
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        return(self.movespeed)
            
            
    def move(self, movespeed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x += self.direction.x * self.movespeed
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.movespeed
        self.collision('vertical')
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                            
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                            
    def update(self):
        self.inputs()
        self.move(self.movespeed)