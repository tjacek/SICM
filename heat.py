import numpy as np
from scipy.integrate import odeint
from scipy.fftpack import diff as psdiff

#def kdv_exact(x, c):
#    u = 0.5*c*np.cosh(0.5*np.sqrt(c)*x)**(-2)
#    return u

#def kdv(u, t, L):
#    ux = psdiff(u, period=L)
#    uxxx = psdiff(u, period=L, order=3)
#    dudt = -6*u*ux - uxxx
#    return dudt

def heat(u,t, L):
    uxx = psdiff(u, period=L, order=2)
#    dudt = -6*u*ux - uxxx
    return uxx

def pde_solution(u0, t, L):
    sol = odeint(heat, u0, t, args=(L,), mxstep=5000)
    return sol


if __name__ == "__main__":
    L = 50.0
    N = 64
    dx = L / (N - 1.0)
    x = np.linspace(0, (1-1.0/N)*L, N)

#    u0 = kdv_exact(x-0.33*L, 0.75) + kdv_exact(x-0.65*L, 0.4)
    u0= np.random.rand(N)

    T = 70
    t = np.linspace(0, T, 501)

    print("Computing the solution.")
    sol = pde_solution(u0, t, L)


    print("Plotting.")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(6,5))
    plt.imshow(sol[::-1, :], extent=[0,L,0,T])
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('t')
    plt.axis('normal')
    plt.title('Heat equation')#'Korteweg-de Vries on a Periodic Domain')
    plt.show()