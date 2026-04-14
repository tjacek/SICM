import numpy as np 

class Quaternion(object):
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def to_list(self):
        return [self.a,self.b,self.c,self.d]

    def to_matrix(self):
        arr=[[ complex(self.a,self.b),
               complex(self.c,self.d)],
             [ complex(-self.c,self.d),
              complex(self.a,-self.b)]]
        return np.array(arr)
    
    @staticmethod
    def from_matrix(arr):
        a=arr[0][0].real
        b=arr[0][0].imag
        c=arr[0][1].real
        d=arr[0][1].imag
        return a,b,c,d

    def __mul__(self,q):
        A=self.to_matrix()
        B=q.to_matrix()
        new_arr=np.dot(A,B)
        new_vec=self.from_matrix(new_arr)
        return Quaternion(*new_vec)

    def __add__(self,q):
        return Quaternion(self.a+q.a, 
                          self.b+q.b, 
                          self.c+q.c, 
                          self.d+q.d )
    
    def __sub__(self,q):
        return Quaternion(self.a-q.a, 
                          self.b-q.b, 
                          self.c-q.c, 
                          self.d-q.d )
    def __repr__(self):
        return f"{self.a},{self.b},{self.c},{self.d}"

    def norm(self):
        total=0
        for x in self.to_list():
            total+= x**2
        return total

def cross_product(a,b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


i=Quaternion(b=1)
j=Quaternion(c=1)
k=Quaternion(d=1)
print(i*i)
print(j*j)
print(k*k)
q=i*j-j*i
print(q.norm())