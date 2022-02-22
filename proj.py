import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 4,3
from matplotlib.animation import FuncAnimation
 
p0x=0.0
p0y=-0.5
p1x=0.0
p1y=0.5
p2x=0.5
p2y=0.0
 
r = 1 # radius of circle
def circle(phi):
    #return np.array([r*np.cos(phi), r*np.sin(phi)])
    return np.array([
        (1.0-phi)**2*p0x + 2*phi*(1.0-phi)*p1x + phi**2*p2x,
        (1.0-phi)**2*p0y + 2*phi*(1.0-phi)*p1y + phi**2*p2y,
        ])
 
# create a figure with an axes
fig, ax = plt.subplots()
# set the axes limits
ax.axis([-1.5,1.5,-1.5,1.5])
# set equal aspect such that the circle is not shown as ellipse
ax.set_aspect("equal")
# create a point in the axes
point, = ax.plot(0,1, marker="o")
 
# Updating function, to be repeatedly called by the animation
def update(phi):
    # obtain point coordinates 
    x,y = circle(phi)
    # set point's coordinates
    point.set_data([x],[y])
    return point,
 
# create animation with 10ms interval, which is repeated,
# provide the full circle (0,2pi) as parameters
ani = FuncAnimation(fig, update, interval=30, blit=True, repeat=True,
                    frames=np.linspace(0,2*np.pi,360, endpoint=False))
 
plt.show()
