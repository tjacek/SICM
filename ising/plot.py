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
    
    def __call__(self, iter_per_spin=500):
        x=[]
        n_iters=np.prod(self.dims)*iter_per_spin
        fun_dict={"energy":np.mean,"std":np.std}
        value_dict={name_i:[] for name_i in fun_dict}
        for i,model_i in enumerate(self.get_models()):
            model_i.step(n_iters)
            energy= model_i.indiv_energy()
            for name_i,fun_i in fun_dict.items():
                value_dict[name_i].append(fun_i(energy))
            x.append(i)
#            y.append(model_i.energy())
        def helper(name_i):     
            y=value_dict[name_i]  
            fig, ax = plt.subplots()
            scatter = ax.plot(x, y)
            plt.xlabel("T")
            plt.ylabel(name_i)
            plt.show()
        helper("energy")
        helper("std")

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
#print(exp)
exp()
