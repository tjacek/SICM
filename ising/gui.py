import pygame as pg
import json
import numpy as np

class GridView(object):
    def __init__(self,grid,cells,step=50):
        self.grid=grid
        self.step=step
        self.cells=cells

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

    def display_dim(self):
        height,width=self.grid.shape
        return self.step*height,self.step*width

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

def init_cells(height,width,step):
    cells=[]
    for i in range(height):
        cells.append([])
        for j in range(width):
            color= int(((i+j) % 3)==0)
            cell_ij=make_cell(i,j,
                              step=step,
                              color=color)
            cells[i].append(cell_ij)
    return cells

def make_grid_view(arr,step=50):
    height,width=arr.shape
    return GridView(grid=arr,
                    cells=init_cells(height,width,step),
                    step=step)

def read_json(in_path):
    with open(in_path, 'r') as file:
        data = json.load(file)
        return data



def exp_loop(in_path:str):
    conf=read_json(in_path)
    pg.init()
    arr=np.ones((conf["height"],conf['width']))
    grid_view = make_grid_view(arr,step=conf['step'])
    window = pg.display.set_mode(grid_view.display_dim())
    clock = pg.time.Clock()
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                point = pg.mouse.get_pos()
                grid_view.flip(point)
                print(point)
        grid_view.show(window)
        pg.display.flip()
        clock.tick(3)
    pg.quit()
    exit()

exp_loop("conf.js")