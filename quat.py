import numpy as np 

class Quaternion(object):
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def to_matrix(self):
        arr=[[ complex(a,b),complex(c,d)],
             [complex(-c,d),complex(a,-b)]]
        return np.array(arr)
    
    @staticmethod
    def from_matrix(self,arr)
        a=self.arr[0][0].real
        b=self.arr[0][0].imag
        c=self.arr[0][1].real
        d=self.arr[0][1].imag
        return a,b,c,d

    def __mul__(self,q):
        A=self.to_matrix()
        B=q.to_matrix()
        new_arr=np.dot(A,B)
        new_vec=self.from_matrix(new_arr)
        return Quaternion(*new_vec)
#        a= self.a*q.a - self.b*q.b - self.c*q.c - self.d*q.d
#        b= self.a*q.b + self.b*q.a + self.c*q.d - self.d*q.c
#        c= self.a*q.c - self.b*q.d + self.c*q.a + self.d*q.b
#        d= self.a*q.d + self.b*q.c - self.c*q.b + self.d*q.a
#        return Quaternion(a,b,c,d)
    
    def __repr__(self):
        return f"{self.a},{self.b},{self.c},{self.d}"

i=Quaternion(b=1)
j=Quaternion(c=1)
k=Quaternion(d=1)
print(i*i)
print(j*j)
print(k*k)