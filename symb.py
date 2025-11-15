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

    def d_t(self):        
        part=[self.eq.diff(q_i)*self.v[i] 
                for i,q_i in enumerate(self.q)]
        part+=[self.eq.diff(v_i)*self.a[i] 
                for i,v_i in enumerate(self.v)]
        eq=part[0]
        for part_i in part[1:]:
            eq+=part_i
        print(eq)

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
    q=make_symbols(['x'])
    v=make_symbols(['v'])
    eq= 0.5*(v[0]**2)-k*(q[0]**2)
    return Langr(q,v,eq)

def orbital():
    q=make_symbols(['ξ','η'])
    v=make_symbols(['v_ξ','v_η'])
    eq= 0.5*(v[0]**2+v[1]**2)
    eq+= 1/sympy.sqrt(q[0]**2+q[1]**2)
    return Langr(q,v,eq)    


f=orbital()
#f.d_t()
print(f.eq)
