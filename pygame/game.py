import pygame

class gameWindow():
    def __init__(self):
        self.window = pygame.display.set_mode((800,600))
        self.caption = pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.fps = 60

    def gameLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.window.fill((0,0,0))
            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()
        quit()
    
    
gameWindow = gameWindow()
gameWindow.gameLoop()