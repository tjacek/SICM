import json
import numpy as np

class Grid(object):
    def __init__(self,height=7,width=7):
        self.height=height
        self.width=width
        self.array=np.ones((height,width))
    
    def randomize(self):
    	for i in range(self.height):
    		for j in range(self.width):
    			p=np.random.uniform(low=0.0, high=1.0)
    			if(p<0.5):
    				self.array[i][j]=-1

    def get_near_values(self,pair):
        return [self.array[x][y] 
            for x,y in self.get_near(pair)]

    def get_near(self,pair):
        x,y=pair
        near=[]
        for x_i in get_cord(x,self.height-1):
            for y_i in get_cord(y,self.width-1):
                near.append((x_i,y_i))
        return near

    def random(self):
        x=np.random.randint(low=self.height,high=None)
        y=np.random.randint(low=self.width,high=None)
        return x,y

    def iter(self):
        for i in range(self.height):
            for j in range(self.width):
                yield i,j

    def size(self):
        return np.product(self.array.shape)
    
    def flip(self,pair_i,p):
        if(np.random.uniform()<p):
            self.array[pair_i]=-1
        else:
            self.array[pair_i]= 1

def get_cord(x,max_value):
    cord=[x]
    if(x<=0):
        cord.append(max_value)
    else:
        cord.append(x-1)
    if(x>=max_value):
        cord.append(0)
    else:
        cord.append(x+1)
    return cord

class Ising(object):
    def __init__(self,grid,
                      J=1,
                      T=5,
                      sampling=None):
        if(type(grid)==tuple or 
           type(grid)==list):
            height,width=grid
            grid=Grid(height=height,
                      width=width)
        if(sampling is None):
            sampling=GibbsSampling()
        if(type(sampling)==str):
            sampling=get_sampling(sampling)
        self.grid=grid
        self.J=J
        self.T=T
        self.sampling=sampling

    def n_spins(self):
        return self.grid.size()

    def b(self,pair):
        values=self.grid.get_near_values(pair)
        values=np.array(values)
        x=self.grid.array[pair]
        return np.sum(self.J*x*values)

    def step(self,n_iters): 
        for i in range(n_iters):
            pair_i=self.grid.random()
            self.sampling(pair_i,self)

    def indiv_energy(self):
        return [self.b(pair_i) 
                    for pair_i in self.grid.iter()]
    
    def energy(self):
        return (-0.5) * np.mean(self.indiv_energy())

class GibbsSampling(object):
    def __call__(self,pair_i,ising):
        x_i=(-2*ising.b(pair_i))/ising.T
        p_i= 1.0/(1.0+np.exp(x_i))
        ising.grid.flip(pair_i,p_i)

    def __str__(self):
        return "gibbs"

class MetropolisSampling(object):
    def __call__(self,pair_i,ising):
        x_i=ising.grid.array[pair_i]
        b_i=ising.b(pair_i)
        delta_E=2*x_i*b_i
        if( delta_E<0):
            ising.grid.array[pair_i]*=(-1)
        else:
            p_i=np.exp(-(delta_E/ising.T))
            ising.grid.flip(pair_i,p_i)

    def __str__(self):
        return "metropolis"

def get_sampling(sampling_type:str):
    sampling_type=sampling_type.lower()
    if(sampling_type=="gibbs"):
        return GibbsSampling()
    if(sampling_type=="metropolis"):
        return MetropolisSampling()    
    raise Exception(f"Unknown sampling:{sampling_type}")

def read_json(in_path):
    with open(in_path, 'r') as file:
        data = json.load(file)
        return data

if __name__ == '__main__':
    grid=Grid()
    grid.randomize()
    print(grid.array)