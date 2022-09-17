import numpy as np

class Langrange(object):
    def __init__(self,fun):
        self.fun=fun

    def __call__(self,path,step=0.01):
        values=path.whole(step)
        return np.sum([self.fun(*value_i) 
                      for value_i in values])

class Free(object):
    def __call__(self,q,v):
        return 0.5*np.dot(v,v)

    def diff_q(self,q,v):
        return 0

    def diff_v(self,q,v):
        return np.sum(v)	

class Harmonic(object):
    def __init__(self,k=1):
        self.k=k 

    def __call__(self,q,v):
        return 0.5*(np.dot(v,v) - self.k*np.dot(q,q))

    def diff_q(self,q,v):
    	return np.sum(q)
    
    def diff_v(self,q,v):
    	return np.sum(v)