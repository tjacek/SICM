import numpy as np
import grid

class Exp(object):
    def __init__(self,dims:tuple,
                      T:float,
                      J:float,
                      iter_per_spin:int,
                      sampling:str):
        self.dims=dims
        self.T=T
        self.J=J
        self.iter_per_spin=iter_per_spin
        self.sampling=sampling
    
    def __call__(self):
        x,y=[],[]
        n_iters=np.prod(self.dims)*self.iter_per_spin
        for i,model_i in enumerate(self.get_models()):
            model_i.step(n_iters)
            x.append(i)
            y.append(model_i.energy())
        print(y)

    def get_models(self):
        sampling_alg=grid.get_sampling(self.sampling)
        for T_i in range(self.T):
            ising_i=grid.Ising(grid=self.dims,
                               J=self.J,
                               T=T_i+1,
                               sampling=sampling_alg)
            ising_i.grid.randomize()
            yield ising_i

def read_exp(in_path):
    if(type(in_path)==str):
        conf=grid.read_json(in_path)
    else:
        conf=in_path
    return Exp(dims=conf['dims'],
               T=conf['T'],
               J=conf['J'],
               iter_per_spin=conf['iter_per_spin'],
               sampling=conf['sampling'])

exp=read_exp("conf_plot.js")
exp()