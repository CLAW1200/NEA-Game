import pygame
import solve

WIDTH = 1500
HEIGHT = 600

#c,m,g,Vx0,Vy0,theta,t0,tmax,steps,outputName

theta = 45
v0 = 10


Vx0, Vy0 = solve.find2part(theta, v0)
pathCoords = solve.main(1.2, 0.500, 9.81, Vx0, Vy0, theta, 0, 2, 180, "test")
xPlot = pathCoords[0]
yPlot = pathCoords[1]
D = pathCoords[4]
H = pathCoords[5]

def nextCoords(i):
    try:
        x = xPlot[i]
        y = yPlot[i]
        x, y = (x/D)*WIDTH, HEIGHT-((y/H)*HEIGHT)
        return x, y
    except IndexError:
        return False

def main():
    pygame.display.set_caption("Cannon")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
     
    coords = 0, HEIGHT
    rect = pygame.Rect(*coords,20,20)
    #sphere = pygame.draw.circle(screen, (255,0,0), coords, 10)
    speed = 5
    next_tick = 500
    i = 0
    colourLim = 100
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        ticks = pygame.time.get_ticks() 
        if ticks > next_tick:
            next_tick += speed
            i += 1
            try:
                rect.topleft = nextCoords(i)
            except TypeError:
                break
        
        if i < colourLim:
            screen.fill((i,8,40))
        else:
            screen.fill((colourLim,8,40))
        screen.fill((255,60,255), rect)
        pygame.display.flip()
        clock.tick(60)
     
    pygame.quit()
 
if __name__ == '__main__':
    main()