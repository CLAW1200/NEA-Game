import pygame
import solve

WIDTH = 800
HEIGHT = 600

#c,m,g,Vx0,Vy0,theta,t0,tmax,steps,outputName

theta = 30
v0 = 20





Vx0, Vy0 = solve.find2part(theta, v0)
pathCoords = solve.main(0.5, 1, 9.81, Vx0, Vy0, theta, 0, 10, 100, "test")
xPlot = pathCoords[0]
yPlot = pathCoords[1]


def nextCoords(i):
    x = xPlot[i]
    y = yPlot[i]
    return x, y


def main():
    pygame.display.set_caption("Oribit")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
     
    coords = 0, HEIGHT
    angle = 90
    rect = pygame.Rect(*coords,20,20)
    speed = 5
    next_tick = 500
    i = 0
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        ticks = pygame.time.get_ticks() 
        if ticks > next_tick:
            next_tick += speed
            i += 1
            rect.topleft = nextCoords(i)
             
        screen.fill((0,0,35))
        screen.fill((0,200,0), rect)
        pygame.display.flip()
        clock.tick(144)
     
    pygame.quit()
 
if __name__ == '__main__':
    main()