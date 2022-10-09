"""calculate the motion of a projectile with air resistance based on the initial velocity, angle, mass, and drag coefficient"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x= 0
y= 0
vx= 50
vy= 50
dt= 0.1
g= 9.81
c= 2
m= 1

def solveForNextPosition(x, y, vx, vy, dt, g, c, m):
    """solve for the next position of the projectile"""
    def deriv(y, t):
        Vx = y[1]
        Vy = y[3]
        return [Vx, -c*Vx/m, Vy, -g-c*Vy/m]
    y0 = [x, vx, y, vy]
    t = [0, dt]
    y = odeint(deriv, y0, t)
    return y[1,0], y[1,2], y[1,1], y[1,3]



xPlot = []
yPlot = []

clockSpeed = 60
for i in range(40):
    try:
        data = solveForNextPosition(x, y, vx, vy, dt, g, c, m)
        x = data[0]
        y = data[1]
        vx = data[2]
        vy = data[3]

        xPlot.append(x)
        yPlot.append(y)

    except:
        break
    
    

#plot the results
print (xPlot)
print (yPlot)
plt.plot(xPlot, yPlot)
plt.show()



