import numpy as np
from scipy import interpolate
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

class Path(object):
    def __init__(self, values,start=None,end=None,
    	    bounds=(0,1),dims=3):
        if(type(values)==int):
            values=np.random.rand(*(dims,values))
        if(start is None):
            start=np.random.rand(dims)
        if(end is None):
            end=np.random.rand(dims)
        step= (bounds[1]-bounds[0])/(values.shape[1]+2)
        self.bounds=bounds
        self.start=start
        self.end=end
        self.values=values
        self.points=np.arange(self.bounds[0],self.bounds[1],step)
        self.interpolate()
        self.dims=dims

    def interpolate(self):
        values=[self.start] + list(self.values.T) + [self.end]
        values=np.array(values).T
        self.splines=[ interpolate.InterpolatedUnivariateSpline(self.points,y_i)
                            for y_i in values]
        self.dervatives=[spline_i.derivative() 
                for spline_i in self.splines]
    
    def reset(self,values):
        self.values=values
        self.interpolate()

    def __call__(self,t):
        return (self.q(t),self.v(t))

    def q(self,t):
        return np.array([ s_i(t) for s_i in self.splines])

    def v(self,t):    	
        return np.array([ d_i(t) for d_i in self.dervatives])

    def whole(self,step=0.01):
    	values=[]
    	for t in self.time(step):
    	    values.append(self(t))
    	return values

    def time(self,step=0.01):
    	diff=self.bounds[1]-self.bounds[0]
    	n=int(diff/step)
    	return [ self.bounds[0]+i*step for i in range(n)]

class Langrange(object):
    def __init__(self,fun):
        self.fun=fun

    def __call__(self,path,step=0.01):
        values=path.whole(step)
        return np.sum([self.fun(*value_i) 
        	          for value_i in values])         	

def EulerVerify(L,path,step=0.01):
    if(type(L)==Langrange):
        L=L.fun
    values=path.whole(step)
    d_q=[L.diff_q(*value_i) 
        for value_i in values]
    d_v=[L.diff_v(*value_i) 
        for value_i in values]
    d_t=np.diff(d_v,prepend=d_v[-1])
    print(np.sum(d_q-d_t))
#    print(d_t)

#def Langrange(step=0.01):
#    def decor_fun(fun):
#        def helper(path):
#            values=path.whole(step)
#            return np.sum([fun(*value_i) 
#        	          for value_i in values])
#        return helper
#    return decor_fun 

#@Langrange(step=0.01)
#def free_particle(q,v):
#    return 0.5*np.dot(v,v)


class Harmonic(object):
    def __init__(self,k=1):
        self.k=k 

    def __call__(self,q,v):
        return 0.5*(np.dot(v,v) - self.k*np.dot(q,q))

    def diff_q(self,q,v):
    	return np.sum(q)
    
    def diff_v(self,q,v):
    	return np.sum(v)

def plot(path:Path,step=0.01):
    q,v= zip(*path.whole(step))
    q=np.array(q)
    if(path.dims==3):
        plot3D(q)
    else:
    	plot2D(q)

def plot3D(q):
    ax = plt.axes(projection='3d')
    xline,yline,zline=q[:,0],q[:,1],q[:,2]
    ax.plot3D(xline, yline, zline, 'gray')
    plt.show()

def plot2D(q):
    x,y=q[:,0],q[:,1]
    plt.plot(x, y) 
    plt.show()	

def optim(L,start,end,n_cand=5,
	  n_points=7,maxiter=10,dims=3):
    path=Path(n_points,start,end,dims=dims)
    init=np.random.uniform(0,1,(n_cand,dims*n_points))
    def loss_fun(x):
        x=np.reshape(x,(dims,n_points))
        path.reset(x)
        value=L(path)
        print(value)
        return value
    bound_w = [(-10, 10)  for _ in range(dims*n_points)]
    result = differential_evolution(loss_fun, bound_w, 
            init=init,maxiter=maxiter, tol=1e-7)
    return path

L=Langrange(Harmonic())
path=optim(L,start=[0,0],
    end=[6.28,0],dims=2,n_points=10)
#plot(path)
EulerVerify(L,path)