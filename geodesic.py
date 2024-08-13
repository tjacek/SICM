from scipy.integrate import odeint
import numpy as np

class ChristoffelSymbols(object):
    def x_det_x(self,x,y):
        return 0,np.sin(y)*np.cos(y)

    def x_det_x(self,x,y):
        return (-np.tan(y)),0

    def x_det_y(self,x,y):
        return (-np.tan(y)),0

    def y_det_y(self,x,y):
        return 0,0

def returns_dydt(y,t):
    dydt = -y * t + 13
    return dydt


y0 = 0
t = np.linspace(0,5,10)
y_result = odeint(returns_dydt, y0, t)

print(y_result)