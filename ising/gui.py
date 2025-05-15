import pygame as pg
import numpy as np
from enum import Enum
import grid

class GridView(object):
    def __init__(self,grid,alg,cells,step=50):
        self.grid=grid
        self.alg=alg
        self.step=step
        self.cells=cells

    def show(self,window):
        for i,cell_i in enumerate(self.cells):
            for j,cell_j in enumerate(cell_i):
                value_ij=(self.grid.array[i][j]<0)
                cell_j.show(window,color=value_ij)

    def get_cord(self,point):
        i= int(point[0]/self.step)
        j= int(point[1]/self.step)
        return i,j 

    def flip(self,point,cord=True):
        if(cord):
            i,j=self.get_cord(point)
        else:
            i,j=point
        self.grid.array[i][j]*=(-1) 

    def flip_near(self,near):
        for i,j in near:
            self.grid.array[i][j]*=(-1)

    def display_dim(self):
        height,width=self.grid.height,self.grid.width
        return self.step*height,self.step*width

class CellColors(Enum):
    live=(0,128,0)
    dead=(128,0,0)

class Cell(object):
    def __init__(self,rect):
        self.rect=rect

    def show(self,window,color):
        if(color):
            color=CellColors.live 
        else:
            color=CellColors.dead 
        pg.draw.rect(window,color.value,self.rect)

def make_cell(i,j,step=50):
    x,y=i*step+i,j*step+j
    rect=pg.Rect(x,y,step,step)
    return Cell(rect)

def init_cells(height,width,step):
    cells=[]
    for i in range(height):
        cells.append([])
        for j in range(width):
            cell_ij=make_cell(i,j,
                              step=step)
            cells[i].append(cell_ij)
    return cells

def make_grid_view(height,
                   width,
                   step=50):
    raw_grid=grid.Grid(height=height,
                       width=width)
    alg=grid.Ising(raw_grid)
    raw_grid.randomize()
    return GridView(grid=raw_grid,
                    cells=init_cells(height,width,step),
                    alg=alg,
                    step=step)

def exp_loop(in_path:str):
    conf=grid.read_json(in_path)
    pg.init()
    grid_view = make_grid_view(height=conf["height"],
                               width=conf["width"],
                               step=conf['step'])

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
#                pair=grid_view.get_cord(point)
                print(point)
                grid_view.alg.step()
#                pair=grid_view.grid.random()
#                print(pair)
#                grid_view.flip(pair,False)
#                near=grid_view.grid.get_near(pair)
#                grid_view.flip_near(near)
        grid_view.show(window)
        pg.display.flip()
        clock.tick(3)
    pg.quit()
    exit()

if __name__ == '__main__':
    exp_loop("conf.js")