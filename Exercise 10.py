from scipy.fftpack import dct,idct
from numpy import*
from numpy.random import randn
import matplotlib.pyplot as plt

def one():
    N =1000
    tau = 1E-6
    def f(t):
        v_1 = 20000
        v_2 = 25000
        return sin(2*pi*v_1*t)+cos(2*pi*v_2*t)

    t = linspace(0,.001,N)
    
    y = f(t)

    plt.plot(t,y)

    def v_k(k):
        return k/(2*N*tau)
    K = v_k(arange(0,N))

    g = dct(y)

    plt.plot(K,abs(g)) #this plot is a little funky, peaks are at the right place tho


    plt.show()
#one()
def two():
    tau = 1E-6
    N =1000

    def f(t):
        v_1 = 20000
        v_2 = 25000
        return sin(2*pi*v_1*t)+cos(2*pi*v_2*t)

    t = linspace(0,.001,N)
    
    y = f(t)
    y_2 = y + .7*randn(N) #add noise
    plt.plot(t,y_2)

    def v_k(k): #frequency array
        return k/(2*N*tau)
    K = v_k(arange(0,N))

    g_2 = dct(y_2)
    plt.plot(K,abs(g_2))

    #have to filter the noise out, vectorization

    def filter_noise(g):
        v_max = max(abs(g))
        for i in range(len(g)): #see if this is right, its copilot
            if abs(g[i]) < v_max:
                g[i] = 0
        return g


    plt.show()
two()

