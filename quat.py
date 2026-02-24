class Quaternion(object):
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def __mul__(self,q):
        a= self.a*q.a - self.b*q.b - self.c*q.c - self.d*q.d
        b= self.a*q.b + self.b*q.a + self.c*q.d - self.d*q.c
        c= self.a*q.c - self.b*q.d + self.c*q.a + self.d*q.b
        d= self.a*q.d + self.b*q.c - self.c*q.b + self.d*q.a
        return Quaternion(a,b,c,d)
    
    def __repr__(self):
        return f"{self.a},{self.b},{self.c},{self.d}"

i=Quaternion(b=1)
j=Quaternion(c=1)
k=Quaternion(d=1)
print(i*i)
print(j*j)
print(k*k)