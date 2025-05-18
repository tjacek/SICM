import numpy as np
import matplotlib.pyplot as plt
import grid

class Exp(object):
    def __init__(self,dims:tuple,
                      T:float,
                      J:float,
                      sampling:str):
        self.dims=dims
        self.T=T
        self.J=J
        self.sampling=sampling
    
    def __call__(self, iter_per_spin=100):
        x,y=[],[]
        n_iters=np.prod(self.dims)*iter_per_spin
        for i,model_i in enumerate(self.get_models()):
            model_i.step(n_iters)
            x.append(i)
            y.append(model_i.energy())
        fig, ax = plt.subplots()
        scatter = ax.plot(x, y)
        plt.xlabel("T")
        plt.ylabel("energy")
        plt.show()

    def get_models(self):
        sampling_alg=grid.get_sampling(self.sampling)
        for T_i in range(self.T):
            ising_i=grid.Ising(grid=self.dims,
                               J=self.J,
                               T=T_i+1,
                               sampling=sampling_alg)
            ising_i.grid.randomize()
            yield ising_i

    def __str__(self):
        width,height=self.dims
        return f"{self.sampling} {width}x{height}" 

def read_exp(in_path):
    if(type(in_path)==str):
        conf=grid.read_json(in_path)
    else:
        conf=in_path
    return Exp(dims=conf['dims'],
               T=conf['T'],
               J=conf['J'],
               sampling=conf['sampling'])

exp=read_exp("conf_plot.js")
print(exp)
#exp()
