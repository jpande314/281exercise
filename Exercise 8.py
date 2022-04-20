from numpy import*
from scipy.integrate import quad
from scipy import special
import matplotlib.pyplot as plt

#25pts
def p_1():
    a = 0
    b = pi
    nn = 200
    x = linspace(0,20,nn+1)
    def besselj1(u,x):
        return cos(u-x*sin(u))
    def simpsons(f,a,b,nn,x):
        u = linspace(a,b,nn+1)
        h = (b-a)/nn 
        weights = 4*ones(nn+1) 
        weights[::2] = 2 
        weights[0] = 1
        weights[-1] = 1
        return (h/3)*sum(weights*f(u,x))
    

    
    range = linspace(0,20,200)
    pt_a = special.jv(1,range)
    pt_b = [(1/pi)*simpsons(besselj1,a,b,nn,x)+.1 for x in x]

    def j1quad(x):
        return (1/pi)*quad(besselj1,0,pi,args=(x))[0]
    
    pt_c = [j1quad(x)+.2 for x in x]

    plt.plot(range,pt_a, color = 'purple', label = 'special.jv')
    plt.plot(x,pt_b, color = 'red', label = 'Simpsons Rule')
    plt.plot(x,pt_c, color = 'orange', label = 'Quad')
    plt.title('3 versions, with translations in height to show all 3')
    plt.legend()
    plt.show()
#p_1()

#20pts
def p_2():
    lam = 500*10^(-9)
    k = 2*pi/lam
    r = linspace(0,10**(-6),100) #function changes with 3rd value\
    #make x,y array, meshgrid
    #convert to r
    n = 1e-6
    x = linspace(-n,n,100)
    y = linspace(-n,n,100)

    
    
    def besselj1(u,r):
        return cos(u-k*r*sin(u))
    @vectorize
    def j1quad(r):
        return (1/pi)*quad(besselj1,0,pi,args=(r))[0]

    xx, yy = meshgrid(x,y)

    r = sqrt(xx**2+yy**2)
    I =((1/pi)*j1quad(r)/(k*r))**2

            
    print(I)
    plt.imshow(I, extent = (-n,n,-n,n))
    plt.show()
p_2()

#20pts
def p_3():
    r = linspace(1,4,2000)
    num_iter = range(0,1001)
    def f(r):
        x = .5
        for i in num_iter:
            x = r*x*(1-x)
        return x
    def g(r,x):
        x_2 = []
    
        for i in num_iter:
            x = r*x*(1-x)
            x_2.append(x)
        return x_2
    m_1 = f(r)
    m_2 = g(r,m_1)
    m_2 = transpose(m_2)
    r = [[r for i in range(1001)] for r in r]
    plt.scatter(r,m_2, s = .0001)
    plt.show()
#p_3()

#do dis after u do 9