import pygame
from pygame.locals import *
import math

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.running = True
        self.cannon = Cannon()
        self.move = False
        self.start()

    def returnMoveState(self):
        return self.move

    def setMoveState(self, move):
            self.move = move

    def start(self):
        while self.running:
            self.run()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.cannon.draw(self.screen)
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.move = True

    def update(self):
        self.cannon.update()

    def run(self):
        self.clock.tick(self.fps)
        self.events()
        self.draw()
        self.update()

class Cannon(pygame.sprite.Sprite, Game):
    def __init__(self):
        self.image = pygame.image.load("images\\cannonTube.png")
        self.image = pygame.transform.rotate(self.image, -15)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 280
        self.angle = 45
        self.move = False
        self.cannonMovImg = self.rot_center(self.image, self.angle)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    
    def pointToMouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.returnMoveState():
            self.rect.center = (mouse_x, mouse_y)
            self.setMoveState(False)
        #aim towards mouse
        else:
            rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            self.cannonMovImg = self.rot_center(self.image, self.angle)
   
  
    def draw(self, screen):
        screen.blit(self.cannonMovImg, self.rect)
    
    def update(self):
        self.pointToMouse()


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("images\\cannonBall.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 280

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        pass


if __name__ == "__main__":
    game = Game(800, 600)
    game.start()
    pygame.quit()