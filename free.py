import numpy as np
from scipy import interpolate

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

#class Path(object):
#    def __init__(self,points,bounds=(0,1)):
#        if(type(points)==tuple):
#            points=np.random.rand(*points)
#        self.points=points
#        self.bounds=bounds
    
#    def __len__(self):
#        return len(self.points)	

#    def __call__(self,t):
#        if(t<self.bounds[0] or t>self.bounds[1]):
#            t=self.bounds[0]
#        return self.points[int(len(self)*t)]

#    def whole(self,step=0.01):
#        return [self(t) for t in self.time(step)]

#    def time(self,step=0.01):
#    	diff=self.bounds[1]-self.bounds[0]
#    	n=int(diff/step)
#    	return [ self.bounds[0]+i*step for i in range(n)]

def get_v(state):
	return state[3:]

def free_particle(state):
	return 0,5*get_v(state)**2

path=Path((7,6))
print(path(0.5))
#state=np,array([1,2,3,4,5,6])
#print(free_particle(state))