import numpy as np
from scipy import interpolate
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

class Path(object):
    def __init__(self, values,start=None,end=None,bounds=(0,1)):
        if(type(values)==int):
            values=np.random.rand(*(3,values))
        if(start is None):
            start=np.random.rand(3)
        if(end is None):
            end=np.random.rand(3)
        step= (bounds[1]-bounds[0])/(values.shape[1]+2)
        self.bounds=bounds
        self.start=start
        self.end=end
        self.values=values
        self.points=np.arange(self.bounds[0],self.bounds[1],step)
        self.interpolate()

    def interpolate(self):
        values=[self.start] + list(self.values.T) + [self.end]
        values=np.array(values).T
        self.splines=[ interpolate.InterpolatedUnivariateSpline(self.points,y_i)
                            for y_i in values]
        self.dervatives=[spline_i.derivative() 
                for spline_i in self.splines]

    def __call__(self,t):
        return np.concatenate([self.q(t),self.v(t)])

    def q(self,t):
        return np.array([ s_i(t) for s_i in self.splines])

    def v(self,t):    	
        return np.array([ d_i(t) for d_i in self.dervatives])

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

def optim(L,start,end,
	    n_cand=5,n_points=7,maxiter=10):
    path=Path(n_points,start,end)
    init=np.random.uniform(0,1,(n_cand,3*n_points))
    def loss_fun(x):
        x=np.reshape(x,(3,n_points))
        return x[0][0]
    bound_w = [(-10, 10)  for _ in range(3*n_points)]
    result = differential_evolution(loss_fun, bound_w, 
            init=init,
            maxiter=maxiter, tol=1e-7)
    return result['x']

L=Lagrangian()
x=optim(L,start=[0,0,0],end=[1,1,1])
print(x)
#path=Path(10,start=[0,0,0],end=[1,1,1])
#plot(path)
#print(path(0.5))