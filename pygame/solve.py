def find2part(theta,V0):
    import math
    theta = math.radians(theta)
    Vx0=V0*math.cos(theta)
    Vy0=V0*math.sin(theta)
    return Vx0,Vy0


def main(c,m,g,Vx0,Vy0,theta,t0,tmax,steps,outputName):

    '''
    The first part of the program sets the initial parameters for an object thrown at some angle above the horizont, including the air resistance dragging effect.
    Then, it solves the differential equation m(dV/dT)=mg-cV, describing the motion ( the numerical solution).
    The second part computes the analytical solution and plots both of them in a x-y plot. 
    The third part creates an animation of the motion and shows the landing point. 

    The new things used are odeint, plots with title, grid and labeled arrow, and animation.
    '''
    from scipy.integrate import odeint
    #import matplotlib.pyplot as plt
    import numpy as np
    import math

    steps = steps*(tmax-t0)

    theta = math.radians(theta)
    

    V0=np.sqrt(Vx0**2+Vy0**2) #Calculates the initial velocity.

    tLF = np.linspace(t0, tmax, steps+1)  # Creates a 1-D array of time values

    y0LF = [0, Vx0, 0, Vy0]  # Creates an array with the initial condition for x-position, velocity along x, y-position, velocity along y.

    def deriv(yLF,tF): #Creates the function which computes the derivatives 
        Vx = yLF[1]   # Identifies the velocity along x axis
        Vy=yLF[3]   #Identifies the velocity along y axis
        return [Vx, -c*Vx/m, Vy, -g-c*Vy/m]   # The function outputs [dx/dt, dVx/dt, dy/dt, dVy/dt]

    yM = odeint(deriv, y0LF, tLF)  #  The 4-D array containing the solution for the differential equation

    
    #plt.plot(yM[:,0],yM[:,2],'.',label='Numerical solution') #Plots y over x numerically.

    #Analytical Solution:
    VT=m*g/c #Calculates the terminal velocity
    plot_x=((V0*VT)/g)*np.cos(theta)*(1-np.exp(-g*tLF/VT)) #calculates dx/dt using the analytical solution
    plot_y=(VT/g)*(V0*np.sin(theta)+VT)*(1-np.exp(-g*tLF/VT))-VT*tLF #calculates dy/dt using the analytical solution


    #Computing answer of the questions:

    i=np.abs(yM[1:steps,2]).argmin() #calculates the point from the y-array closest to 0 (after the initial point)and assigns it to i (=impact).

    D=yM[i+1,0] #Computes the distance to the point of impact.

    H=np.amax(yM[:,2]) #Finds the max value of the array plot_y, which represents the highest point of the trajectory and assigns it to H.

    TF=tLF[i+1]

    Vxi=yM[i+1,1]
    Vyi=yM[i+1,3]
    Vi=np.sqrt(Vxi**2+Vyi**2)

    #Creates the file .txt and saves the answers of the questions
    f=open(f'{outputName}.txt','w')
    f.write(f' The distance to the point of impact is {D} m.\n\nThe highest point of the trajectory is at {H} meters above ground.\n\nThe time for flight is {TF} s.\n\nThe impact velocity is {Vi} m/s.\n\nThe terminal velocity is {VT} m/s.')
    f.close()


    return plot_x, plot_y, D, H, TF, Vi, yM, steps

if __name__ == "__main__":
    pass