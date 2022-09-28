import pygame
import solve2
import math

WIDTH = 800
HEIGHT = 600

class Cannon(pygame.sprite.Sprite):
    def __init__ (self, x, y, width, height):
        #import cannon image
        self.image = pygame.image.load("images\\cannonTube.png")
        #get rect
        self.rect = self.image.get_rect()
        #set position
        self.rect.x = x
        self.rect.y = y
        #set width and height
        self.width = width
        self.height = height
        #set x and y
        self.x = x
        self.y = y

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.rect.x, self.rect.y = rel_x, rel_y        


    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Projectile(pygame.sprite.Sprite):
    def __init__ (self, x, y, width, height):
        self.vx = 300
        self.vy = 300


        #import cannon image
        self.image = pygame.image.load("images\\cannonBall.png")
        #get rect
        self.rect = self.image.get_rect()
        #set position
        self.rect.x = x
        self.rect.y = y
        #set width and height
        self.width = width
        self.height = height
        #set x and y
        self.x = x
        self.y = y

    def fire(self):
        output = solve2.solveForNextPosition(self.rect.x,self.rect.y,self.vx,self.vy,1/60,9.8,2,1)
        self.rect.x = output[0]
        self.rect.y = output[1]
        self.vx = output[2]
        self.vy = output[3]



    def update(self):  

        #if mouse is clicked, set projectile to move
        if pygame.mouse.get_pressed()[0]:
            self.fire()
        else:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
            self.rect.x, self.rect.y = rel_x, rel_y

    

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Cannon")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.cannon = Cannon(0, 0, 0, 0)
        self.projectile = Projectile(0, 0, 0, 0)
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.cannon.update()
        self.projectile.update()

    def draw(self):
        self.screen.fill((0, 30, 30))
        self.cannon.draw(self.screen)
        self.projectile.draw(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
