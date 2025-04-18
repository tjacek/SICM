import numpy as np

class Grid(object):
    def __init__(self,height=7,width=7):
        self.height=height
        self.width=width
        self.array=np.ones((height,width))

    def get_near(self,pair):
        i,j=pair
        if( (i<0 or self.height<i) or 
            (j<0 or self.width<j)):
        	return None
        near=[]
        x_lower,x_upper=(0<i),i<(self.height-1)
        y_lower,y_upper=(0<j),j<(self.width-1)
        if(x_lower):
            near.append((i-1,j))
        if(x_upper):
            near.append((i+1,j))        	
        if(y_lower):
            near.append((i,j-1))
        if(y_upper):
            near.append((i,j+1))
        if(x_lower and y_lower):
            near.append((i-1,j-1))
        if(x_upper and y_upper):
            near.append((i+1,j+1))        
        if(x_lower and y_upper):
            near.append((i-1,j+1))
        if(x_upper and y_lower):
            near.append((i+1,j-1))
        return near

grid=Grid()
print(grid.array)
print(grid.get_near((0,0)))