import pygame as pg
import numpy as np

class GridView(object):
    def __init__(self,grid,step=50):
        self.grid=grid
        self.step=step
        heigh,width=self.grid.shape
        self.cells=[]
        for i in range(heigh):
            self.cells.append([])
            for j in range(width):
                color= int(((i+j) % 3)==0)
                cell_ij=make_cell(i,j,
                                 step=self.step,
                                 color=color)
                self.cells[i].append(cell_ij)

    def show(self,window):
        for i,cell_i in enumerate(self.cells):
            for j,cell_j in enumerate(cell_i):
                value_ij=self.grid[i][j]
                cell_j.show(window,color=value_ij)

    def get_cord(self,point):
        i= int(point[0]/self.step)
        j= int(point[1]/self.step)
        return i,j 

    def flip(self,point):
        i,j=self.get_cord(point)
        old_value=self.grid[i][j]
        self.grid[i][j]= (old_value+1)%2

class Cell(object):
    def __init__(self,rect,color=(255,0,0)):
        self.rect=rect
        self.color=color

    def show(self,window,color):
        if(color):
            color=(0,128,0)
        else:
            color=(128,0,0)
        pg.draw.rect(window, color, self.rect)

def make_cell(i,j,step=50,color=False):
    if(color):
        color=(0,128,0)
    else:
        color=(128,0,0)
    x,y=i*step+i,j*step+j
    rect=pg.Rect(x,y,step,step)
    return Cell(rect,color)

pg.init()
window = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
input_box = GridView(np.ones((10,10)))
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
                point = pg.mouse.get_pos()
                input_box.flip(point)
                print(point)
    input_box.show(window)
    pg.display.flip()
    clock.tick(3)

pg.quit()
exit()