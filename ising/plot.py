import numpy as np
import matplotlib.pyplot as plt
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
    
    def n_iters(self):
        return np.product(self.dims)*self.iter_per_spin

    def __call__(self):
#        fun_dict={"energy":np.mean,"std":np.std}
#        value_dict={name_i:[] for name_i in fun_dict}
        energy,std=[],[]
        for i,model_i in enumerate(self.get_models()):
            print(model_i)
            energy_i=self.iter_energy(model_i)
            energy.append(np.mean(energy_i))
            std.append(np.std(energy_i))
#            for name_j,fun_j in fun_dict.items():
#                value_dict[name_j].append(fun_j(energy_i))
    
        fig, ax = plt.subplots()
        ax.errorbar(x=list(range(len(energy))),
                     y=energy, 
                     yerr=std, fmt='-o')
        plt.show()
#        for name_i,x_i in value_dict.items():
#            simple_plot(x=x_i,
#                    xlabel="T",
#                    ylabel=name_i)

    def get_models(self):
        sampling_alg=grid.get_sampling(self.sampling)
        for T_i in range(self.T):
            ising_i=grid.Ising(grid=self.dims,
                               J=self.J,
                               T=T_i+1,
                               sampling=sampling_alg)
            ising_i.grid.randomize()
            yield ising_i
    
    def single_iter(self,T=5,iter_per_spin=100):
        ising=grid.Ising(grid=self.dims,
                               J=self.J,
                               T=T,
                               sampling=self.sampling)
        energy=self.iter_energy(ising)
        simple_plot(x=energy,
                    xlabel="n_iters",
                    ylabel="energy")    
    
    def iter_energy(self,ising,burn_out=0.33):
        n_iters=self.n_iters()
        energy=[]
        for i in range(n_iters):
            ising.step(1)
            energy_i=ising.energy()
            energy.append(energy_i)
        energy=np.array(energy)
        stable=int(n_iters*burn_out)
        return energy[stable:]
    
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
               iter_per_spin=conf['iter_per_spin'],
               sampling=conf['sampling'])

def simple_plot(x,
                y=None,
                xlabel="T",
                ylabel="energy"):
    if(y is None):
        y=x
        x=list(range(len(y)))
    fig, ax = plt.subplots()
    scatter = ax.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

exp=read_exp("conf_plot.js")
#print(exp)
exp()
#print(exp.single_iter())
