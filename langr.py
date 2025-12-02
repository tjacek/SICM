import numpy as np
import matplotlib.pyplot as plt
import sympy

class Langrange1D(object):
    def __init__(self,q,v,eq):
        self.q=q
        self.v=v
        self.eq=eq
    
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
        t=[ step*i for i in range(n)]
        eq=self.q.subs(self.defaults)
        x=[eq.subs(self.t, t_i) 
            for t_i in t]
        print(x)
        plt.plot(t,x)
        plt.ylabel('x')
        plt.xlabel('t')
        plt.show()

def harmonic_path():
    A=sympy.symbols("A") 
    w=sympy.symbols("ω")
    theta=sympy.symbols("θ")
    q= A*sympy.cos(w*Path1D.t) + theta
#    [(A,1),(w,1),(theta,0)]
    return Path1D(q,{"A":1,"ω":1,"θ":0})

def linear_path():
    a=sympy.symbols("a") 
    b=sympy.symbols("b")    
    return Path1D(A*sympy.cos(a*Path1D.t + b))

def harmonic_langr():
    k=sympy.symbols("k") 
    m=sympy.symbols("m") 
    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)-0.5*k*(q**2)
    return Langrange1D(q,v,eq)

def linear_langr():
    m=sympy.symbols("m") 
    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)
    return Langrange1D(q,v,eq)

def gravity_langr():
    m=sympy.symbols("m") 
    g=sympy.symbols("g") 

    q=sympy.symbols('q')
    v=sympy.symbols('v')
    eq= 0.5*m*(v**2)-m*g*x
    return Langrange1D(q,v,eq)

path=harmonic_path()
path.plot_x()
#L=harmonic_langr()
#print(L.langr_euler(path))
