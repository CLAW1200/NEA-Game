import pygame
import solve
import math

WIDTH = 800
HEIGHT = 600

#c,m,g,Vx0,Vy0,theta,t0,tmax,steps,outputName

theta = 20
v0 = 7


Vx0, Vy0 = solve.find2part(theta, v0)
pathCoords = solve.main(1.2, 0.500, 9.81, Vx0, Vy0, theta, 0, 12, 180, "test")
xPlot = pathCoords[0]
yPlot = pathCoords[1]
D = pathCoords[4]
H = pathCoords[5]

class Cannon(pygame.sprite.Sprite):
    def __init__ (self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        
        

    def update(self):
        #move image by 1px

               
        #point towards mouse
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
        self.cannon = Cannon(0, 0, 40, 10)
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

    def draw(self):
        self.screen.fill((0, 30, 30))
        self.cannon.draw(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
