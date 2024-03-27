import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm

class Pendulum(object):
    def __init__(self,l=1.0,
    	              m=1.0,
    	              g=9.8):
        self.l=l 
        self.m=m
        self.g=g

    def __call__(self,v,theta):
    	L=0.5*self.m*(self.l**2)*(v**2)
    	L-= self.m*self.g*np.cos(theta)
    	return L


delta = 0.1
v = np.arange(-20.0, 20.0, delta)
theta = np.arange(-np.pi, np.pi,  np.pi/360)
X, Y = np.meshgrid(theta, v)

hamil = np.vectorize(Pendulum())
Z=hamil(X,Y)
print(hamil(X,Y))
#Z1 = np.exp(-X**2 - Y**2)
#Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
#Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')

plt.show()