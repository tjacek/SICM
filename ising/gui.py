import pygame as pg
import numpy as np

class GridView(object):
    def __init__(self,grid):
        self.grid=grid
        heigh,width=self.grid.shape
        self.cells=[]
        for i in range(heigh):
            self.cells.append([])
            for j in range(width):
                color= int(((i+j) % 3)==0)
                cell_ij=make_cell(i,j,color=color)
                self.cells[i].append(cell_ij)

    def show(self,window):
        for cell_i in self.cells:
            for cell_j in cell_i:
                cell_j.show(window)

class Cell(object):
    def __init__(self,rect,color=(255,0,0)):
        self.rect=rect
        self.color=color

    def show(self,window):
        pg.draw.rect(window, self.color, self.rect)

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
    input_box.show(window)
    pg.display.flip()
    clock.tick(3)

pg.quit()
exit()