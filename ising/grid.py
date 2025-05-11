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

    def get_near(self,pair):
        x,y=pair
        near=[]
        for x_i in get_cord(x,self.height-1):
            for y_i in get_cord(y,self.width-1):
                near.append((x_i,y_i))
        return near

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

if __name__ == '__main__':
    grid=Grid()
    grid.randomize()
    print(grid.array)
#print(grid.get_near((0,0)))