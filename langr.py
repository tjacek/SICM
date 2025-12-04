import numpy as np
import matplotlib.pyplot as plt
import sympy

class Langrange1D(object):
    def __init__(self,q,v,eq,defaults=None):
        self.q=q
        self.v=v
        self.eq=eq
        self.defaults=defaults
    
    def derv(self ,derv_vars):
        syb_var=self.eq
        for var_i in derv_vars:
            syb_var=syb_var.diff(var_i)
        return syb_var

    def d_x(self):
        return self.eq.diff(self.q)
    
    def d_v(self):
        return self.eq.diff(self.v)

    def langr_euler(self,path):
        d_x= path.curry(self.d_x())
        d_v_t= path.curry(self.d_v()).diff("t")
        return d_x - d_v_t

    def action(self,path,lim=None):
        f=path.curry(langr)
        if(lim is None):
            return sympy.integrate(f,self.t)
        else:
            t_0,t_1=lim
            return  sympy.integrate(f,(self.t,t_0,t_1))

    def plot(self,lim_q=(-100,100),lim_v=(-100,100),steps=64):
        q_lin=np.linspace(lim_q[0], lim_q[1], steps)
        v_lin=np.linspace(lim_v[0], lim_v[1], steps)
        z_eq=self.eq.subs(self.defaults) 
        Z=[[float(z_eq.subs([("q",q_i),("v",v_i)]))
             for q_i in q_lin]
                 for v_i in v_lin  ] 
        Z=np.array(Z)
        X, Y = np.meshgrid(q_lin, v_lin)
        levels = np.linspace(np.min(Z),np.max(Z),10)
        fig, ax = plt.subplots()
        ax.contour(X, Y, Z, levels=levels)
        plt.xlabel("q")
        plt.xlabel("v")
        plt.show()

class Path1D(object):
    t=sympy.symbols("t")
    def __init__(self,q,defaults=None):
        self.q=q
        self.v=q.diff("t")
        self.defaults=defaults

    def curry(self,eq):
        rep_vars=[("q",self.q),("v",self.v)]
        return eq.subs(rep_vars)
    
    def plot_x(self, n=100,step=0.1):
        self.plot(self.q,"x",n,step)
    
    def plot_v(self, n=100,step=0.1):
        self.plot(self.v,"v",n,step)
    
    def plot( self,
              eq,
              ylabel="x",
              n=100,
              step=0.1):
        t=[ step*i for i in range(n)]
        if(self.defaults):
            eq=eq.subs(self.defaults)
        x=[eq.subs(self.t, t_i) 
            for t_i in t]
        plt.plot(t,x)
        plt.ylabel(ylabel)
        plt.xlabel('t')
        plt.show()

def harmonic_path():
    A=sympy.symbols("A") 
    w=sympy.symbols("ω")
    theta=sympy.symbols("θ")
    q= A*sympy.cos(w*Path1D.t) + theta
    return Path1D(q,{"A":1,"ω":1,"θ":0})

def linear_path():
    a=sympy.symbols("a") 
    b=sympy.symbols("b")    
    q=a*Path1D.t + b
    return Path1D(q,{"a":1,"b":1})

def harmonic_langr():
    k=sympy.symbols("k") 
    m=sympy.symbols("m") 
    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)-0.5*k*(q**2)
    defaults={"k":1,"m":2}
    return Langrange1D(q,v,eq,defaults)

def linear_langr():
    m=sympy.symbols("m") 
    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)
    defaults={"m":2}
    return Langrange1D(q,v,eq,defaults)

def gravity_langr():
    m=sympy.symbols("m") 
    g=sympy.symbols("g") 

    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)-m*g*x
    return Langrange1D(q,v,eq)

print(np.linspace(-3, 3, 16))

#path=linear_path()
#path.plot_x()
#path.plot_v()
L=linear_langr()
L.plot()
#print(L.langr_euler(path))



#X, Y = np.meshgrid(np.linspace(-3, 3, 16), np.linspace(-3, 3, 16))
#Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
#levels = np.linspace(np.min(Z), np.max(Z), 7)
#fig, ax = plt.subplots()

#ax.contour(X, Y, Z, levels=levels)

#plt.show()