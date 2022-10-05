import pygame
import math

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.mouse1down = False
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_SPACE:
                    cannon.fire()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse1down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse1down = False
    
    def update(self):
        cannon.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        cannon.draw(self.screen)
        pygame.display.update()



class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("images\\cannonTube.png")
        self.image = pygame.transform.rotate(self.image, -15)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 280
        self.angle = 45
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
        if game.mouse1down:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.center = (mouse_x, mouse_y)
   
  
    def draw(self, screen):
        screen.blit(self.cannonMovImg, self.rect)
    
    def update(self):
        self.pointToMouse()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("images\\cannonBall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = cannon.angle
        self.speed = 5
        self.x_speed = self.speed * math.cos(math.radians(self.angle))
        self.y_speed = self.speed * math.sin(math.radians(self.angle))
        self.gravity = 0.5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y -= self.y_speed
        self.y_speed -= self.gravity

        if self.rect.y > 600:
            self.kill()



if __name__ == "__main__":
    game = Game(600, 600)   
    cannon = Cannon()
    game.run()
