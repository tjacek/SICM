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

    def get_models(self):
        for T_i in range(self.T):
            ising_i=grid.Ising(grid=self.dims,
                               J=self.J,
                               T=T_i+1,
                               sampling=self.sampling)
            yield ising_i

def read_exp(in_path):
    conf=grid.read_json(in_path)
    return Exp(dims=conf['dims'],
               T=conf['T'],
               J=conf['J'],
               sampling=conf['sampling'])

exp=read_exp("conf_plot.js")
print(exp.T)