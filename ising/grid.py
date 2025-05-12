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
    def __init__(self,grid,J=1,T=5):
        self.grid=grid
        self.J=J
        self.T=T

    def b(self,pair):
        values=self.grid.get_near_values(pair)
        values=np.array(values)
        x=self.grid.array[pair]
        return np.sum(self.J*x*values)

    def step(self):
        pair_i=self.grid.random()
        x_i=(-2*self.b(pair_i))/self.T
        p_i= 1.0/(1.0+np.exp(x_i))
        if(np.random.uniform()<p_i):
            self.grid.array[pair_i]= -1
        else:
            self.grid.array[pair_i]= 1


if __name__ == '__main__':
    grid=Grid()
    grid.randomize()
    print(grid.array)