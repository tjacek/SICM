import sympy

class Harmonic(object):
    def	__init__(self,k=1.0):
        self.q=sympy.symbols('q')
        self.v=sympy.symbols('v')
        self.k=k
        self.eq= 0.5*(self.v**2 + self.k*self.q**2)

        q_eq=sympy.diff(self.eq,self.q)
        self.diff_q=sympy.lambdify(self.q, q_eq, "numpy") 
        q_eq=sympy.diff(self.eq,self.q)
        self.diff_q=sympy.lambdify(self.q, q_eq, "numpy") 
        v_eq=sympy.diff(self.eq,self.v)
        self.diff_v=sympy.lambdify(self.v, v_eq, "numpy") 


L=Harmonic()
print(L.diff_q(2.4))
print(L.diff_v(5))