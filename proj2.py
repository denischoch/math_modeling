from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np
 
tau=np.linspace(0,1,1000)
P=np.array([[180, 290],
           [140, 335],
           [50,  170],
           [10,   15],
           [360, 240],
           [140,  67]
           ])
 
def Bezier(t, P):
    # Bezier Matrix:
    Mb=np.matrix([
        [ -1,   5, -10,  10, -5, 1],
        [  5, -20,  30, -20,  5, 0],
        [-10,  30, -30,  10,  0, 0],
        [ 10, -20,  10,   0,  0, 0],
        [ -5,   5,   0,   0,  0, 0],
        [  1,   0,   0,   0,  0, 0]
                 ])
    # T matrix
    xx, yy=np.meshgrid(np.arange(5, -1, -1), t)
    xx=np.matrix(xx)
    yy=np.matrix(yy)
    T_mat=np.power(yy, xx)
    B=T_mat*Mb*P
    return B
%matplotlib qt5
fig = plt.figure()
plt.xlim(0,600)
plt.ylim(0,600)
X,Y=Bezier(tau, P)[:,0],Bezier(tau, P)[:,1]
camera = Camera(fig)
 
for i in range(100):
    coord=Bezier(i/100, P)
    plt.plot(X,Y,color = '#ff0000')
    plt.scatter(coord[0,0], coord[0,1], color = '#00ff00' , marker='o')
    camera.snap()
    
animation = camera.animate(interval = 200, repeat = True,
                           repeat_delay = 500)

