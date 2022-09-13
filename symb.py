import sympy

class Harmonic(object):
    def	__init__(self,k=1.0):
        self.q=sympy.symbols('q')
        self.v=sympy.symbols('v')
        self.k=k
        self.eq= 0.5*(self.v**2 + self.k*self.q**2)
        self.diff_q=sympy.diff(self.eq,self.q)
        self.diff_v=sympy.diff(self.eq,self.v)

L=Harmonic()
print(L.diff_q)
print(L.diff_v)