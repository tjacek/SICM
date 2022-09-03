import numpy as np
from scipy import interpolate
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class Path(object):
    def __init__(self, values,bounds=(0,1)):
        if(type(values)==tuple):
            values=np.random.rand(*values)
        step= (bounds[1]-bounds[0])/values.shape[1]
        self.bounds=bounds
        self.values=values
        self.points=np.arange(self.bounds[0],self.bounds[1],step)
        self.splines=self.interpolate()

    def interpolate(self):
        return [ interpolate.InterpolatedUnivariateSpline(self.points,y_i)
                    for y_i in self.values]

    def __call__(self,t):
        return np.array([ s_i(t) for s_i in self.splines])

    def whole(self,step=0.01):
        return np.array([self(t) for t in self.time(step)])

    def time(self,step=0.01):
    	diff=self.bounds[1]-self.bounds[0]
    	n=int(diff/step)
    	return [ self.bounds[0]+i*step for i in range(n)]

class Lagrangian(object):
    def __init__(self,fun=None):
        if(fun is None):
            fun=free_particle
        self.fun=fun

    def __call__(self,path,step=0.01):
        values=path.whole(step)
        return np.sum([ self.fun(value_i) 
        	  for value_i in values])

def free_particle(state):
    v=state[3:]
    return 0.5*np.dot(v,v)

def plot(path:Path,step=0.01):
    ax = plt.axes(projection='3d')
    data= path.whole(step)
    xline=data[:,0]
    yline=data[:,1]
    zline=data[:,1]
    ax.plot3D(xline, yline, zline, 'gray')
    plt.show()

L=Lagrangian()

path=Path((6,7))
print(L(path))
#state=np,array([1,2,3,4,5,6])
#print(free_particle(state))