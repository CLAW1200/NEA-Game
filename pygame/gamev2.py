import pygame
import math
import solve2

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.mouse1down = False
        self.spacedown = False
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
                    self.spacedown = True

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse1down = True

                if event.button == 4:
                    cannon.angle += 3
                    cannon.cannonMovImg = cannon.rot_center()

                if event.button == 5:   
                    cannon.angle -= 3
                    cannon.cannonMovImg = cannon.rot_center()
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse1down = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.spacedown = False
    
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
        self.angle = 90
        self.cannonMovImg = self.rot_center()
        self.fireCannon = False
        

    def rot_center(self):
        """rotate an image while keeping its center and size"""
        image = self.image
        angle = self.angle
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

    def fire(self):
        if game.spacedown:
            self.fireCannon = True
            self.ball = Projectile(self.rect.center[0], self.rect.center[1], self.angle)

    def draw(self, screen):
        screen.blit(self.cannonMovImg, self.rect)
        if self.fireCannon:
            self.ball.draw(screen)


    def update(self):
        self.fire()
        self.pointToMouse()
        if self.fireCannon:
            self.ball.update()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        self.image = pygame.image.load("images\\cannonBall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.speed = 50
        self.x_speed = self.speed * math.cos(math.radians(self.angle))
        self.y_speed = self.speed * math.sin(math.radians(self.angle))
        self.gravity = 9.81

        self.calcX = 0
        self.calcY = 0
        self.calcVx = self.x_speed
        self.calcVy = self.y_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        data = solve2.solveForNextPosition(self.rect.x, self.rect.y, self.x_speed, self.y_speed, 1, self.gravity, 0.1, 1)
        self.calcX = data[0]
        self.calcY = data[1]
        self.calcVx = data[2]
        self.calcVy = data[3]

        #transform the calculation coords to screen coords
        self.rect.x = self.calcX
        self.rect.y = self.calcY



        if self.rect.y > 600:
            self.kill()

    def kill(self):
        del self

if __name__ == "__main__":
    game = Game(600, 600)   
    cannon = Cannon()
    game.run()