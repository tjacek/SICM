import sympy

class Langr(object):
    def __init__(self,q,v,eq):
        self.q=q
        self.v=v
        self.eq=eq

    def d_q(self):
        return [self.eq.diff(q_i)
                 for q_i in self.q]
    def d_v(self):
        return [self.eq.diff(v_i)
                 for v_i in self.v]

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

#class Harmonic1D(object):
#    def __init__(self,k=1.0):
#        self.q=sympy.symbols("x")
#        self.v=sympy.symbols("v")
#        self.k=k
#        self.eq= 0.5*(self.v**2)
#        self.eq+= self.k*(self.q**2)

#class Harmonic(object):
#    def	__init__(self,k=1.0):
#        self.q=make_symbols(['x','y'])
#        self.v=make_symbols(['v_x','v_y'])
#        self.k=k
#        self.eq= 0.5*(self.v[0]**2+self.v[1]**2)
#        self.eq+= self.k*(self.q[0]**2+self.q[1]**2)

#    def L_22(self):
#        mat=[[self.eq.diff(v_i).diff(v_j) 
#                 for v_i in self.v]
#                    for v_j in self.v]
#        return mat

#    def L_12(self):
#        mat=[[self.eq.diff(v_i).diff(q_j) 
#                 for v_i in self.v]
#                    for q_j in self.q]
#        return mat

#    def L_1(self):
#        return [self.eq.diff(q_i) 
#                    for q_i in self.q ]
    
#    def L_2(self):
#        return [self.eq.diff(v_i) 
#                    for v_i in self.v ]



#        q_eq=sympy.diff(self.eq,self.q)
#        self.diff_q=sympy.lambdify(self.q, q_eq, "numpy") 
#        q_eq=sympy.diff(self.eq,self.q)
#        self.diff_q=sympy.lambdify(self.q, q_eq, "numpy") 
#        v_eq=sympy.diff(self.eq,self.v)
#        self.diff_v=sympy.lambdify(self.v, v_eq, "numpy") 

#L=Harmonic()
#print(L.diff_q(2.4))
#print(L.diff_v(5))

f=harmonic1D()
print(f.d_v())
