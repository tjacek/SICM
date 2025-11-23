import sympy

class Langr(object):
    def __init__(self,q,v,eq):
        self.q=q
        self.v=v
        self.a=derv_var(self.q)
        self.eq=eq

    def d_q(self):
        return [self.eq.diff(q_i)
                 for q_i in self.q]
    def d_v(self):
        return [self.eq.diff(v_i)
                 for v_i in self.v]

    def d_t_v(self):
        v=self.d_v()
        return [ self.d_t(v_i) for v_i in v]
    
    def d_t(self, eq):        
        part=[eq.diff(q_i)*self.v[i] 
                for i,q_i in enumerate(self.q)]
        part+=[eq.diff(v_i)*self.a[i] 
                for i,v_i in enumerate(self.v)]
        eq_t=part[0]
        for part_i in part[1:]:
            eq_t+=part_i
        return eq_t

    def curry(self,path):
        v=path.diff("t")
        rep_vars=[("x",path),("v",v)]
        return self.eq.subs(rep_vars)

class Path(object):
    t=sympy.symbols("t")
    def __init__(self,cord_eqs):
        self.x_cord=cord_eqs
        self.v_cord=[x_i.diff("t") 
                for x_i in self.x_cord]

    def dims(self):
        return len(self.x_cord)

    def curry(self,langr):
        q_names=[q_i.name for q_i in langr.q]
        rep_vars=list(zip(q_names,self.x_cord))
        v_names=[v_i.name for v_i in langr.v]
        rep_vars+=list(zip(v_names,self.v_cord))
        return langr.eq.subs(rep_vars)

    def action(self,langr,lim=None):
        f=self.curry(langr)
        if(lim is None):
            return sympy.integrate(f,self.t)
        else:
            t_0,t_1=lim
            return  sympy.integrate(f,(self.t,t_0,t_1))


def derv_var(q):
    return [sympy.symbols(q_i.name+"_a") 
               for q_i in q]

def make_symbols(names):
    return [sympy.symbols(name_i) 
              for name_i in names]

def harmonic(k=1.0,m=1.0):
    q=make_symbols(['x','y'])
    v=make_symbols(['v_x','v_y'])
    eq= 0.5*(v[0]**2+v[1]**2)-k*(q[0]**2+q[1]**2)
    return Langr(q,v,eq)

def harmonic1D(k=1.0,m=1.0):
    k=sympy.symbols("k") 
    m=sympy.symbols("m") 
    q=make_symbols(['x'])
    v=make_symbols(['v'])
    eq= 0.5*m*(v[0]**2)-0.5*k*(q[0]**2)
    return Langr(q,v,eq)

def pendulum():
    q=make_symbols(['θ'])
    v=make_symbols(['v_θ̇'])
    u=sympy.symbols("u") 
    m=sympy.symbols("m")     
    l=sympy.symbols("l") 
    g=sympy.symbols("g")
    eq=0.5*m*l*l*v[0]*v[0]
    eq+=m*l*g* sympy.cos(v[0])
    return Langr(q,v,eq)

def orbital():
    u=sympy.symbols("u") 
    m=sympy.symbols("m") 
    q=make_symbols(['ξ','η'])
    v=make_symbols(['v_ξ','v_η'])
    eq= 0.5*m*(v[0]**2+v[1]**2)
    eq+= u/sympy.sqrt(q[0]**2+q[1]**2)
    return Langr(q,v,eq)    


f=harmonic1D()
 
#path= 3*t+5
path=Path([sympy.sin(Path.t)])

print(path.action(f,(0,2*3.14)))

#f.d_t()
#print(f.d_q())
#print(f.d_v())
#print(f.d_t_v())