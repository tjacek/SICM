import numpy as np

class Path(object):
    def __init__(self,points,bounds=(0,1)):
        if(type(points)==tuple):
            points=np.random.rand(*points)
        self.points=points
        self.bounds=bounds
    
    def __len__(self):
        return len(self.points)	

    def __call__(self,t):
        if(t<self.bounds[0] or t>self.bounds[1]):
            t=self.bounds[0]
        return self.points[int(len(self)*t)]

def get_v(state):
	return state[3:]

def free_particle(state):
	return 0,5*get_v(state)**2

path=Path((7,6))
print(path(0.6))
#state=np,array([1,2,3,4,5,6])
#print(free_particle(state))