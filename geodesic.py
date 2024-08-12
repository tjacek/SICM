from scipy.integrate import odeint
import numpy as np

def returns_dydt(y,t):
    dydt = -y * t + 13
    return dydt


y0 = 0
t = np.linspace(0,5,10)
y_result = odeint(returns_dydt, y0, t)

print(y_result)